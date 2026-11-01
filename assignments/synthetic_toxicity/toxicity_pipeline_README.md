# Synthetic Toxicity Data — Noising/Denoising Pipeline

This directory contains the **evaluation and training datasets** for a T5-based Nepali text denoising pipeline, derived from the [Rakshak: Toxic Content Benchmark](https://huggingface.co/datasets/biraj-bhusal/rakshak-nepali-toxicity-final) (Biraj Bhusal et al., 2024).

## Pipeline Overview

```
noisy.csv  ──▶  devanagari_unaware.csv  ──▶  nepali_aware_final.csv
 (input)         (Stage 1 output)            (Stage 2 output)
```

| File | Role | Description |
|------|------|-------------|
| `noisy.csv` | **T5 Input** | Raw, unmodified social media text — Roman Nepali, English, code-mixed, Devanagari. First 500 rows from Rakshak. |
| `devanagari_unaware.csv` | **Stage 1 Target** | Blind script transliteration — all non-Devanagari converted to Devanagari without grammar awareness. English is transliterated (e.g., `"Proud"` → `"प्राउड"`), not translated. Word order preserved exactly. |
| `nepali_aware.csv` | **Annotation Layer** | Intermediate file with grammar annotations (`_combine`, `_needshalanta`, `_incorrect`, etc.) showing what fixes are needed to go from unaware to aware. Not a model target — a reference for human annotators. |
| `nepali_aware_final.csv` | **Stage 2 Target** | Grammar-aware natural Nepali — English translated (not transliterated), postpositions joined, halantas added, spellings corrected. Social media handles (`@user_123`) kept in Latin. |

## Model Workflow & Quality Assurance

The dataset was curated and verified using a multi-agent model pipeline:
- **Translation / Nepalification**: Gemini 3.6 Flash
- **Translation Review & Auditing**: DeepSeek v4
- **Final Correction & Fixes**: Gemini 3.6 Flash (High)

## Annotation Tags (used in `nepali_aware.csv`)

| Tag | Meaning | Example |
|-----|---------|---------|
| `_combine` | Should be joined with adjacent word | `सरकार ले` → `सरकारले` |
| `_needshalanta` | Needs विराम (halanta) | `हुन्छन` → `हुन्छन्` |
| `_incorrect` | Misspelled word | `थिक` → `ठिक` |
| `_break` | Should be separated | `आफुलाइजे` → `आफूलाई जे` |
| `_english_nepali` | English word with Nepali equivalent | `प्राउड_garva` |

## Data Statistics

- **Rows**: 500 (truncated from 4,805 for feasibility)
- **Source**: `biraj-bhusal/rakshak-nepali-toxicity-final` (CC-BY-4.0)

## Key Findings

- People often write Romanized Nepali with suffixes detached (e.g., `sarkar le` instead of `sarkarle`)
- Compound words frequently break in informal writing
- Code-mixed English terms need meaningful Nepali translation, not just Devanagari transliteration
