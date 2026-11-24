# Case Study Simulation: Nepali Grammar Checker (Bal & Shrestha, 2007)

# --- 0. KNOWLEDGE BASE (LEXICON) ---
lexicon = {
    "केटा": {"pos": "NN", "gender": "M"}, # NN: Noun, M: Masculine
    "केटी": {"pos": "NN", "gender": "F"}, # F: Feminine
    "घर": {"pos": "NN", "gender": "N"},   # N: Neutral
    "जान्छ": {"pos": "VB", "agrees_with_gender": "M"}, # VB: Verb
    "जान्छे": {"pos": "VB", "agrees_with_gender": "F"}
}

# --- 1. TOKENIZER MODULE ---
def tokenize(sentence):
    print("--- Phase 1: Tokenization ---")
    tokens = sentence.replace("।", "").strip().split()
    print(f"Output: {tokens}\n")
    return tokens

# --- 2. POS TAGGER & MORPHOLOGY MODULE ---
def tag_and_analyze(tokens):
    print("--- Phase 2/3: Tagging & Morphology ---")
    tagged = []
    for t in tokens:
        info = lexicon.get(t, {"pos": "UNK"}).copy()
        info['word'] = t
        tagged.append(info)
    print(f"Output: {tagged}\n")
    return tagged

# --- 3. CHUNKER MODULE ---
def chunk(tagged):
    print("--- Phase 4: Chunking ---")
    chunks = []
    for info in tagged:
        if info['pos'] == 'NN': chunks.append(('NP', info))
        elif info['pos'] == 'VB': chunks.append(('VP', info))
    print(f"Output: {chunks}\n")
    return chunks

# --- 4. SYNTAX CHECKER MODULE ---
def check_syntax(chunks):
    print("--- Phase 5/6: Syntax Verification ---")
    subject = next((c[1] for c in chunks if c[0] == 'NP'), None)
    verb = next((c[1] for c in chunks if c[0] == 'VP'), None)
    
    if subject and verb:
        if subject.get('gender') != verb.get('agrees_with_gender'):
            error = f"Grammar Error: Subject '{subject['word']}' ({subject['gender']}) mismatches Verb '{verb['word']}' ({verb['agrees_with_gender']})"
            print(f"Output: {error}\n")
            return error
    print("Output: Correct Syntax\n")
    return None

# --- 5. SUGGESTION MODULE ---
def suggest(error):
    if not error: return
    print("--- Phase 7: Correction Suggestion ---")
    # Simple logic: Swap verb form
    correction_map = {"जान्छ": "जान्छे", "जान्छे": "जान्छ"}
    for wrong, right in correction_map.items():
        if wrong in error:
            print(f"Suggestion: Replace '{wrong}' with '{right}'\n")

# --- EXECUTION ---
def run_pipeline(sentence):
    print(f"Analyzing: {sentence}")
    tokens = tokenize(sentence)
    tagged = tag_and_analyze(tokens)
    chunks = chunk(tagged)
    error = check_syntax(chunks)
    suggest(error)

if __name__ == "__main__":
    run_pipeline("केटी घर जान्छ ।")
    run_pipeline("केटा घर जान्छ ।")
