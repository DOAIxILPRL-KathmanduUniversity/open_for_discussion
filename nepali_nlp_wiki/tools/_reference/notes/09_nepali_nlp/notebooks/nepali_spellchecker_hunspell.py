# !pip install spylls
from spylls.hunspell import Dictionary

# Note: Requires ne_NP.aff and ne_NP.dic files
def check_spelling(word, dic_path="./ne_NP"):
    try:
        dictionary = Dictionary.from_files(dic_path)
        is_correct = dictionary.lookup(word)
        suggestions = list(dictionary.suggest(word)) if not is_correct else []
        return is_correct, suggestions
    except:
        return "Error: Dictionary files not found.", []

if __name__ == "__main__":
    # print(check_spelling("नेपला"))
    pass
