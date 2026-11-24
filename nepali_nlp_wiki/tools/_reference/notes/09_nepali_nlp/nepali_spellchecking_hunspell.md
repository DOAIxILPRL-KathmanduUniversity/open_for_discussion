# Case Study: Nepali Spellchecker (Hunspell/Spylls)

> [!IMPORTANT] Gist
> Since it is impossible to list every possible Nepali word, we utilize the **Hunspell** paradigm: a compact dictionary of root words (`.dic`) combined with a set of morphological affix rules (`.aff`).

## 1. The Hunspell Paradigm
- **.dic (Dictionary File)**: Contains headwords (roots).
- **.aff (Affix File)**: Defines prefixes and suffixes that can be attached to roots to form valid words.
- **Example**: If `घर` is in `.dic` and `हरू` is a valid suffix in `.aff`, the word `घरहरू` is recognized as correct.

## 2. Implementation with `spylls`
The `spylls` library allows Python to interface with standard LibreOffice/OpenOffice Nepali dictionaries.
```python
from spylls.hunspell import Dictionary
dictionary = Dictionary.from_files('./ne_NP')
is_correct = dictionary.lookup("नेपाल") # True
```

## 3. Error Detection & Correction
- **Lookup**: Verifying if a word exists in the expanded root+affix space.
- **Suggestions**: Calculating edit distances and applying affix rules to suggest the closest valid word for a typo (e.g., `नेपला` -> `नेपाल`).
- **Limitation**: This is a purely morphological check; it does not verify grammatical context (e.g., it accepts `भात म खान्छु` even if the syntax is unusual).

---

**Notebook**: [nepali_spellchecker_hunspell.py](notebooks/nepali_spellchecker_hunspell.py)

#nepali-nlp #spellcheck #hunspell #morphology #spylls #libreoffice
