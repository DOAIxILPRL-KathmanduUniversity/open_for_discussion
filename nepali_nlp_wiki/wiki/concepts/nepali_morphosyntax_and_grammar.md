---
okf_version: "0.2"
type: "concept"
title: "Nepali Morphosyntax & Lexical Grammar"
description: "Foundational analysis of Nepali morphosyntactic structures: agglutinative nominal case markers (vibhakti), honorific verbal paradigms, compound verbs, and wordnet synset relations for NLP systems."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T11:50:00Z"
tags:
  - morphology
  - syntax
  - case-markers
  - honorifics
  - compound-verbs
  - wordnet
---

# Nepali Morphosyntax & Lexical Grammar

## Overview
Nepali is an SOV (Subject-Object-Verb), head-final Indo-Aryan language characterized by agglutinative postpositional case marking, complex verbal inflection for tense-aspect-mood and honorific tiers, and extensive compound verb serialization.

---

## 1. Syntactic Architecture & Paninian Karaka Theory

Constituent word order in Nepali is relatively free and scrambleable (canonical SOV, but OSV and OVS permutations are discourse-valid):
- **SOV**: रामले भाइलाई पुस्तक दियो (*Rām-le bhāi-lāi pustak diyo*)
- **OSV**: भाइलाई रामले पुस्तक दियो (*Bhāi-lāi Rām-le pustak diyo*)
- **OVS**: पुस्तक दियो भाइलाई रामले (*Pustak diyo bhāi-lāi Rām-le*)

Because grammatical dependencies reflect semantic relationships between nominal entities and the verbal predicate rather than rigid configurational phrase structures, Nepali computational syntax is effectively modeled using **Paninian Karaka Theory**:

| Karaka | Sanskrit Name | Semantic Role & Case Marking | Example |
| :--- | :--- | :--- | :--- |
| **कर्ता** | *Kartā* | Primary agent/actor initiating the action (Ergative *-le* or unmarked). | **रामले** भात खायो (*Rām-le*) |
| **कर्म** | *Karma* | Patient/entity most affected by action (Accusative/Dative *-lāi* or unmarked). | रामले **भाइलाई** बोलायो (*bhāi-lāi*) |
| **करण** | *Karaṇa* | Instrument, tool, or medium used to achieve action (*-le*, *-dvārā*, *-mārfat*). | **कलमले** लेख्यो (*kalam-le*) |
| **सम्प्रदान** | *Sampradāna* | Beneficiary or recipient of the action (*-lāi*, *-kā lāgi*, *-kā nimitta*). | **गरिबलाई** दियो (*garib-lāi*) |
| **अपादान** | *Apādāna* | Source, origin, or point of spatial/temporal separation (*-bāṭa*, *-dekhi*). | **रूखबाट** खस्यो (*rūkh-bāṭa*) |
| **अधिकरण** | *Adhikaraṇa* | Spatial, temporal, or conceptual locus/substrate (*-mā*, *-māthi*, *-bhitra*). | **कोठामा** बस्यो (*koṭhā-mā*) |

*Note on Sambandha (सम्बन्ध / Genitive):* Genitive markers (*-ko, -kā, -kī*) denote nominal-to-nominal modification (*रामको पुस्तक*) rather than direct verbal dependency, and are categorized as modifier relations.

Syntactic well-formedness in dependency parsing requires satisfying the classical triad:
1. **आकाङ्क्षा (Ākāṅkṣā - Expectancy)**: Transitive verbs inherently demand a Kartā and Karma to complete semantic realization.
2. **योग्यता (Yogyatā - Semantic Fitness)**: Nominal fillers must possess real-world plausibility (preventing semantically aberrant constructs).
3. **सन्निधि (Sannidhi - Structural Proximity)**: Modifiers and clause elements must operate within valid discourse-structural boundaries.

---

## 2. Split Ergativity & Case Postpositions (विभक्ति / Vibhakti)

Nepali displays classic **morphosyntactic split ergativity**, governed by the interaction between **verbal transitivity** and **aspect/tense**:
- **Intransitive Verbs** (*जानु, सुत्नु, आउनु*): Ergative *-le* is strictly **forbidden** across all tenses (*राम गयो*, never \**रामले गयो*).
- **Transitive Verbs in Past / Perfective Aspect** (*खायो, लेखेको छ*): Ergative *-le* is **mandatory** (*रामले भात खायो*).
- **Transitive Verbs in Non-Past / Imperfective Aspect** (*खान्छ, लेख्दै छ*): Ergative *-le* is **optional** (*राम/रामले भात खान्छ*).
- **Dative Experiencer Subjects**: Non-volitional physiological and emotional states govern dative marking (*-lāi*) on the logical subject rather than ergative (*मलाई भोक लाग्यो* - "To me hunger occurred"; *उसलाई रिस उठ्यो*).

### Agglutinative Clitic Stacking Order (विभक्ति संकलन)
Devanagari orthography attaches postpositions directly to stems following a rigid, non-commutative morpheme sequence:
$$\text{Stem} \ \oplus \ [\text{Plural } \text{-हरू}] \ \oplus \ [\text{Case Postposition}] \ \oplus \ [\text{Emphatic / Focus Particle}]$$
- घर $\rightarrow$ **घरहरू** (Stem + Plural)
- घरहरू $\rightarrow$ **घरहरूलाई** (Stem + Plural + Dative)
- घरहरूलाई $\rightarrow$ **घरहरूलाई पनि** (Stem + Plural + Dative + Focus Particle)
- घरहरू $\rightarrow$ **घरहरूबाटै** (Stem + Plural + Ablative + Emphatic *-ai*)

---

## 3. Honorific Agreement Tiers (आदरार्थी / Aadararthak)

Verbal conjugations in Nepali strictly encode the social distance and status of the subject:
- **Low Honorific (अनादर / Anādar)**: Used for intimate younger relations or animals (तँ / *tã* $\rightarrow$ गर्छस् / *garchhas*).
- **Medium Honorific (मध्यम आदर / Madhyam Ādar)**: Standard informal dialogue among peers (तिमी / *timī* $\rightarrow$ गर्छौ / *garchhau*).
- **High Honorific (उच्च आदर / Uchha Ādar)**: Respectful formal communication (तपाईं / *tapāī̃* $\rightarrow$ गर्नुहुन्छ / *garnuhunchha*).
- **Royal / Extra-High Honorific (महा आदर / Mahā Ādar)**: Formal literary and monarchical registers (हजुर / *hajur* $\rightarrow$ गरिबक्सिन्छ / *garibaksinchha*).

Handling these honorific shifts is a primary challenge in Machine Translation and Dialog Systems (e.g. English *you* has 4+ distinct functional translations).

---

## 4. Compound Verbs & Serialization (संयुक्त क्रिया)

Nepali frequently serializes a main verb root with a secondary auxiliary vector verb (*halnu*, *dinu*, *saknu*, *chhadnu*) to express aspectual nuances:
- **Completive / Exhaustive**: खाइसक्यो (*khāi-sakyo* - completely finished eating)
- **Decisive / Telic**: खाइहाल्यो (*khāi-hālyo* - ate immediately / without hesitation)
- **Continuative / Habitual**: खाइराख्यो (*khāi-rākhyo* - kept on eating)
- **Benefactive / Other-Oriented**: खाइदियो (*khāi-diyo* - ate away for someone else)
- **Exploratory / Tentative**: खाइहेर्‍यो (*khāi-heryo* - tasted / tried eating)

---

## 5. Lexical Semantics & IndoWordNet

Lexical representation in Nepali computational systems maps nouns, verbs, adjectives, and adverbs into **Synsets (Synonym Sets)**:
- **Hypernymy & Hyponymy**: Superordinate and subordinate hierarchical links (e.g. *सवारीसाधन* is hypernym to *बस*, *कार*).
- **Meronymy & Holonymy**: Part-whole relationships (e.g. *पाङ्ग्रा* / wheel is meronym of *गाडी* / vehicle).
- Linked directly to the Hindi and Princeton English WordNets via shared synset IDs within the IndoWordNet framework.

---

## Connected Graph Nodes
- **Phonology**: [Devanagari Phonology & Orthography](wiki/concepts/devanagari_phonology_and_orthography.md)
- **Datasets**: [Morphology & POS Datasets](wiki/datasets/morphology_pos_datasets.md), [Lexicons & WordNet Datasets](wiki/datasets/lexicon_wordnet_datasets.md)
- **Papers**: [Morphology & POS Papers](wiki/papers/morphology_pos_papers.md), [WordNet & WSD Papers](wiki/papers/wordnet_wsd_papers.md)

