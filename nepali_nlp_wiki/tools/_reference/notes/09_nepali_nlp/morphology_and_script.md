# Nepali Morphology & Script

## Devanagari Script
- 36 consonants (व्यंजन), 12 vowels (स्वर)
- Matras (vowel diacritics) attach to consonants
- Conjuncts (संयुक्त अक्षर) — half-forms for consonant clusters

## Morphological Rules
- **Agglutinative Suffixing**: Root + suffixes for tense/aspect/mood.
    - Example: गर् (do) → गर्छ (does), गर्यो (did), गर्नेछ (will do).
- **Causative forms**: खाउ → खुवाउ → खुवाउनु.
- **Compounding**: Many words formed by combining roots (e.g., कामकाज).

## Case Marking System (विभक्ति)
Nepali is a **relatively free word order** language. Grammatical roles are primarily identified by **suffixes (case markers)** attached to nouns.

| Case | Marker (Suffix) | Example | Role / Note |
| :--- | :--- | :--- | :--- |
| **Nominative** | -ले (le) / Ø | रामले गोली खेल्छ | Default subject case. |
| **Accusative** | -लाई (lāi) / Ø | सीतालाई लिएर गए | Direct object. |
| **Dative** | -लाई (lāi) | बालकलाई पुस्तक दिए | Indirect object. Overlaps with Accusative. |
| **Genitive** | -को/-की/-का | रामको छोरा | Possession (Singular/Fem/Plural variants). |
| **Instrumental**| -ले (le) / -द्वारा | चम्चाले भात खाए | Means or tool used for action. |
| **Ergative** | -ले (le) | रामले भात खायो | Subject of transitive verb in **past tense**. |
| **Locative** | -मा (mā) | घरमा छ | Place or location. |
| **Ablative** | -बाट (bāta) | घरबाट आए | Point of origin or separation. |

> [!TIP] Parsing Hint
> Because of free word order, identifying the `Ergative` marker is crucial for establishing the **agent** in past-tense transitive sentences.

## Formality Levels
- Low (तँ), mid (तिमी), high (तपाईं), royal (हजुर)
- Verb conjugation changes with each level

- Handle irregular verbs as exceptions

## 4. Research Landscape: Morphological Analysis
The development of computational morphology for Nepali has spanned over two decades, evolving from simple affix stripping to complex neural analyzers:

- **Foundational Infrastructure (2005-2011)**:
    - **Hardie et al. (2005, 2009)**: Established the Nelralec Tagset (NT-01) and the first automated morphosyntactic schemes.
    - **Balaram Prasain (2011)**: Delivered the most comprehensive computational analysis of Nepali morphology (PhD Thesis), serving as the theoretical base for subsequent tools.
    - **Bal Krishna Bal**: Developed the first widely accessible Morphological Analyzer and Stemmer.
- **Task-Specific Analyzers (2012-2017)**:
    - **Rai & Bhat (2012)**: Focused on building a robust morphological analyzer.
    - **Chhetri et al. (2015)**: Specialized analysis for Nepali nouns.
    - **Borah et al. (2017)**: Specialized analysis for non-declinable adjectives.
- **Sanskrit & Modern Enhancements (2020-2021)**:
    - **Adhikari & Neupane (2020)**: Introduced vowel-based splitting to handle complex Sanskrit-borrowed words (Tatsama).
    - **Bhutia et al. (2021)**: Advanced verb morphological analyzer for complex conjugations.
    - **Yadav & Shakya (2020)**: Neural-based morphological analyzers using deep learning.

---

#nepali #morphology #linguistics
