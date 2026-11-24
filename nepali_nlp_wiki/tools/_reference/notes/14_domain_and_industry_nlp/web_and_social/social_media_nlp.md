# Social Media NLP

> [!IMPORTANT] Gist
> Social media NLP deals with "non-traditional" text that is short, noisy, multilingual, and rich in metadata. It requires specialized pre-processing and adaptation of classic IE and classification tools (Farzindar & Inkpen, 2020).

## 1. Linguistic Pre-processing
Social media text (Tweets, Posts) requires normalization before standard NLP tools can be used:
- **Text Normalization**: Mapping non-standard words (e.g., "u", "brb", "gr8") to their canonical forms.
- **Tokenization**: Handling hashtags (`#NLP`), mentions (`@user`), and emojis which carry semantic weight.
- **Dialect Identification**: Crucial for languages like Arabic where social media users often write in local dialects rather than Modern Standard Arabic (MSA).

## 2. Semantic Analysis & Intelligence
- **Geo-location Detection**: Predicting a user's location based on:
    - **Network Infrastructure**: IP addresses or check-ins.
    - **Network Structure**: Analyzing the locations of the user's social circle.
    - **Content-based**: Identifying location-specific terms or local events in the text.
- **Event & Topic Detection**: Identifying specified (e.g., planned protests) vs. unspecified (e.g., sudden earthquakes) events in real-time.
- **Rumor Detection**: Classifying information as truthful, false, or unverified based on propagation patterns and source reliability.

## 3. High-Stakes Social Media Applications
- **Healthcare**: Monitoring **Adverse Drug Reactions (ADR)** by mining patient experiences posted online.
- **Disaster Response**: Emergency situation awareness to assist first responders by extracting actionable insights from social streams.
- **Finance**: Predicting market sentiment and voting intentions by analyzing the "collective consciousness" of the digital world.

---

#social-media #geo-location #rumor-detection #normalization #ie
