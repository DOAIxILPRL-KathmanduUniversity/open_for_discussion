import streamlit as st
import pandas as pd
from spylls.hunspell import Dictionary
import pathlib
import json

# Load the ne_NP dictionary
path = pathlib.Path(__file__).parent / 'ne_NP/ne_NP'
dictionary = Dictionary.from_files(str(path))


# Function to analyze a word and return its analysis
def analyze_word(word):
    is_correct = dictionary.lookup(word)
    suggestions = list(dictionary.suggest(word)) if not is_correct else []
    good_forms = list(dictionary.lookuper.good_forms(word))
    return is_correct, suggestions, [str(form) for form in good_forms] if good_forms else []


# Function to load custom dictionary
def load_custom_dictionary():
    try:
        with open('custom_dictionary.json', 'r', encoding='utf-8') as f:
            return set(json.load(f))
    except FileNotFoundError:
        return set()


# Function to save custom dictionary
def save_custom_dictionary(custom_dict):
    with open('custom_dictionary.json', 'w', encoding='utf-8') as f:
        json.dump(list(custom_dict), f, ensure_ascii=False)


# Function to analyze text
def analyze_text(text, custom_dictionary):
    words = text.split()
    results = []
    for word in words:
        if word in custom_dictionary:
            results.append({"Word": word, "Spelling": "Correct (Custom)", "Suggestions": [], "Good Forms": []})
        else:
            is_correct, suggestions, good_forms = analyze_word(word)
            results.append({
                "Word": word,
                "Spelling": "Correct" if is_correct else "Incorrect",
                "Suggestions": suggestions,
                "Good Forms": good_forms
            })
    return results


# Load custom dictionary
custom_dictionary = load_custom_dictionary()

# Streamlit UI
st.set_page_config(page_title="Nepali Spell Checker", page_icon="🇳🇵", layout="wide")

st.title("🇳🇵 Nepali Spell Checker and Text Analyzer")
st.write("Enter Nepali text manually or upload a CSV file for spell-checking and analysis.")

# Input method selection
input_method = st.radio("Choose input method:", ("Manual Entry", "CSV Upload"))

if input_method == "Manual Entry":
    # Text area input for manual entry
    text = st.text_area("Enter your Nepali text here:", height=200)
    if text:
        results = analyze_text(text, custom_dictionary)
else:
    # File uploader for CSV
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

        # Allow user to select a column
        selected_column = st.selectbox("Select a column to analyze:", df.columns)

        # Initialize session state for row index if not exists
        if 'row_index' not in st.session_state:
            st.session_state.row_index = 0

        # Navigation buttons
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("Previous"):
                st.session_state.row_index = max(0, st.session_state.row_index - 1)
        with col3:
            if st.button("Next"):
                st.session_state.row_index = min(len(df) - 1, st.session_state.row_index + 1)

        # Display current row index
        st.write(f"Current row: {st.session_state.row_index + 1} / {len(df)}")

        # Get the text from the selected column and row
        text = str(df.iloc[st.session_state.row_index][selected_column])

        # Analyze the text
        results = analyze_text(text, custom_dictionary)

if 'results' in locals():
    # Display the original text
    st.subheader("Original Text:")
    st.write(text)

    # Display the results
    st.subheader("Analysis Results:")
    for i, result in enumerate(results):
        col1, col2, col3, col4 = st.columns([2, 2, 3, 3])

        with col1:
            st.write(f"**{result['Word']}**")

        with col2:
            if result['Spelling'] == "Incorrect":
                corrected_word = st.selectbox(f"Correction for '{result['Word']}'",
                                              [result['Word']] + result['Suggestions'],
                                              key=f"correction_{i}")
                if corrected_word != result['Word']:
                    results[i]['Word'] = corrected_word
            else:
                st.write(f"_{result['Spelling']}_")

        with col3:
            if result['Suggestions']:
                st.write(f"Suggestions: {', '.join(result['Suggestions'])}")

        with col4:
            if result['Good Forms']:
                st.write(f"Good Forms: {', '.join(result['Good Forms'])}")

        st.write("---")

    # Display corrected text
    corrected_text = " ".join([result['Word'] for result in results])
    st.subheader("Corrected Text:")
    st.write(corrected_text)

# Custom dictionary management (in sidebar)
st.sidebar.header("Custom Dictionary")
new_word = st.sidebar.text_input("Add a new word:")
if st.sidebar.button("Add to Dictionary"):
    if new_word:
        custom_dictionary.add(new_word)
        save_custom_dictionary(custom_dictionary)
        st.sidebar.success(f"Added '{new_word}' to the custom dictionary.")

st.sidebar.subheader("Current Custom Words:")
st.sidebar.write(", ".join(custom_dictionary) if custom_dictionary else "No custom words yet.")

# Additional information about the dictionary and algorithms
with st.expander("Dictionary and Algorithm Details"):
    st.write(
        "The dictionary contains entries from the ne_NP dictionary, including word forms, affixes, and spelling rules.")
    st.write("**Correctness Check:** Validates if a word is correct according to the dictionary rules.")
    st.write(
        "**Suggestion Algorithm:** Provides suggestions for misspelled words based on similarity and possible corrections.")
    st.write("**String Processing:** Handles string operations to generate valid word forms and check spelling.")

st.info("This app demonstrates the power of the Spylls library, leveraging Hunspell's spell checking capabilities.")