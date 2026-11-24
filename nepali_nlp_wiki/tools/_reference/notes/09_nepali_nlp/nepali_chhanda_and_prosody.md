# Masterclass: Nepali Chhanda & Prosody Detection

> [!IMPORTANT] Gist
> Nepali literature and music are deeply rooted in **Chhanda** (metrical patterns). Detecting these automatically involves syllabification, assigning Laghu (L) / Guru (G) weights, and calculating metrical similarity against a database of classical patterns.

## 1. The Chhanda Pipeline
Detecting a meter in lyrics requires a multi-step linguistic engine:

1.  **Text Cleaning**: Removing non-Devanagari characters and normalizing whitespace.
2.  **Syllabification**: Splitting words into syllables based on vowel-consonant clusters.
3.  **LG Weighting**: 
    *   **Laghu (L)**: Short vowels (अ, इ, उ, ऋ).
    *   **Guru (G)**: Long vowels (आ, ई, ऊ, ए, ऐ, ओ, औ) or syllables followed by conjuncts/anusvara.
4.  **Pattern Matching**: Comparing the resulting LG signature (e.g., `LLG LLG LLG`) against a database using **Levenshtein Distance** or **Regex**.

## 2. Technical Implementation: Line-by-Line Analysis
Lyrics rarely follow a single chhanda perfectly throughout. A robust analysis should process text **line-by-line**:
- **Confidence Bins**: Categorizing matches into similarity ranges (e.g., 90-100% for strict classical adherence, 50-70% for folk variants).
- **The "No Match" Challenge**: Many modern lyrics are free-verse (*Gadhya*) and will result in 0% confidence against classical databases.

## 3. Visualization & Rendering
Plotting chhanda distributions in Devanagari requires specialized font configuration in Matplotlib:
- **Font**: Use `Nakula` or `Noto Sans Devanagari`.
- **Logic**: Explicitly register the `.ttf` path to avoid rendering "tofu" blocks.

---

**Notebook**: [nepali_chhanda_analysis.py](notebooks/nepali_chhanda_analysis.py) (Metrical Analysis Engine)

#nepali #chhanda #prosody #linguistics #syllabification #lyrics-analysis
