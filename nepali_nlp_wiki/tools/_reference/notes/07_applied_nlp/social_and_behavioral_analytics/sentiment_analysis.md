# Sentiment Analysis & Opinion Mining

> [!IMPORTANT] Gist
> Sentiment analysis is the computational study of opinions, sentiments, and emotions expressed in text. It aims to identify the **polarity** (positive/negative) and **target** (what is being talked about) of subjective content (Liu, 2010).

## 1. Sentiment Levels
- **Document Level**: Classifying the entire document as positive or negative (e.g., a movie review).
- **Sentence Level**: Determining the sentiment of individual sentences. Distinguishes between **Objective** (facts) and **Subjective** (opinions) sentences.
- **Aspect/Feature Level**: Identifying opinions on specific aspects of an entity (e.g., "The *battery life* of this phone is great, but the *screen* is dim").

## 2. Sentiment Classification Types
- **Supervised Classification**: Training a model (SVM, Naive Bayes, CNN) on a labeled corpus of reviews (e.g., IMDB dataset).
- **Unsupervised/Lexicon-Based**: Using a predefined sentiment dictionary (like SentiWordNet) to calculate a score based on the sum of word polarities.

## 3. Latent Aspect Rating Analysis (LARA)
Advanced sentiment mining for reviews (Zhai & Massung, 2016):
1.  **Aspect Identification**: Discovering latent aspects (e.g., "Food," "Service," "Ambiance") from a collection of hotel reviews using topic models.
2.  **Aspect Rating**: Estimating the user's hidden rating for each specific aspect, even if they only provided a single overall star rating.
3.  **Weight Estimation**: Determining how much each aspect contributed to the user's overall satisfaction (e.g., did they give 4 stars because of the "Food" or the "Price"?).

## 3. Sentiment Lexicons
- **SentiWordNet**: An extension of WordNet where synsets are assigned scores for positivity, negativity, and objectivity.
- **VADER**: A parsimony rule-based model specifically tuned for social media sentiment (handles emojis, punctuation, and intensifiers).

## 4. Subjectivity Analysis
Distinguishing between fact and opinion is a prerequisite for accurate sentiment analysis.
- **Subjective**: "The movie was a boring waste of time."
- **Objective**: "The movie was directed by Christopher Nolan."
- Systems often use a **Subjectivity Classifier** to filter text before performing sentiment analysis.

## 5. Challenges
- **Sarcasm & Irony**: "Oh great, another flat tire."
- **Domain Dependence**: "Small" is positive for a camera but negative for a hotel room.
- **Negation Handling**: "Not good" vs. "not bad."
- **Comparative Opinions**: "Entity A is better than Entity B."

---

#applied #sentiment #opinion-mining #subjectivity
