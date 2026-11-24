# Multilingual & Low-Resource NLP

> [!IMPORTANT] Gist
> Multilingual models enable knowledge transfer from high-resource languages (e.g., English) to low-resource ones (e.g., Twi, Nepali, Kazakh), bridging the "Digital Divide" (Azunre, 2021).

## 1. Cross-Lingual Transfer
- **Zero-Shot Transfer**: Training a model on one language and testing it on another without any target-language training data.
- **mBERT (Multilingual BERT)**: Pre-trained on 104 languages. It maps different languages into a shared vector space, allowing for cross-lingual task transfer.
- **Cross-Lingual LM (XLM)**: Uses a Translation Language Modeling (TLM) objective to improve alignment between parallel sentences.

## 2. Low-Resource Strategies
- **Pre-trained Tokenizer Transfer**: Using an existing multilingual tokenizer but fine-tuning it on target monolingual data (e.g., transferring mBERT to Twi data).
- **Training from Scratch**: If the target language script or morphology is too distinct, training a domain-specific tokenizer and model from scratch is often superior.
- **Back-Translation**: Creating synthetic parallel data by translating target language text back into the source language to augment training sets.

## 3. Benchmarks
- **XGLUE / XTREME**: Standard benchmarks for evaluating the cross-lingual generalization of models across diverse tasks (NER, QA, Sentiment).

---

#domain-specific #multilingual #low-resource #mbert #xlm
