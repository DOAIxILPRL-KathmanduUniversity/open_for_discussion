"""
🇳🇵 अध्याय १: डिजिटल टेक्स्ट डेटाको परिचय (प्रयोगात्मक अभ्यास)
-------------------------------------------------------
यस नोटबुकमा हामी NLP का आधारभूत अवधारणालाई कोडमार्फत बुझ्नेछौं।
"""

import re
import nltk
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# --- १. कम्प्युटरको दृष्टिकोण: अक्षर र शब्द ---
sentence = "रामले स्याउ खायो।"
chars = list(sentence)
words = sentence.split()

print("१. डिजिटल प्रतिनिधित्व:")
print(f"अक्षरहरू: {chars}")
print(f"शब्दहरू (Tokens): {words}\n")

# --- २. टेक्स्टको तथ्याङ्क (NLTK प्रयोग गरेर) ---
text = """
नेपाल एक सुन्दर देश हो। नेपालको राजधानी काठमाडौँ हो।
काठमाडौँ मन्दिरहरूको सहर पनि हो। नेपाल सरकारले पर्यटन विकासमा
ध्यान दिनुपर्छ। देशको विकास र समृद्धि सबै नेपालीको चाहना हो।
"""
# सफाइ
clean_text = re.sub(r'[।(),?]', '', text)
tokens = clean_text.split()
freq = Counter(tokens)

print("२. शब्द आवृत्ति (Word Frequency):")
print(freq.most_common(5))

# --- ३. Bag-of-Words (Vectorization) ---
corpus = [
    "नेपाल पदयात्राको लागि उत्कृष्ट गन्तव्य हो।", # पर्यटन
    "सरकारले नयाँ सडक बनाउनेछ।",                # विकास
    "हिमाल आरोहण गर्न पर्यटक आउँछन्।",          # पर्यटन
    "शिक्षा क्षेत्रमा बजेट बढाइएको छ।"          # विकास
]
labels = ["पर्यटन", "विकास", "पर्यटन", "विकास"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print("\n३. Bag-of-Words म्याट्रिक्स:")
print(X.toarray())
print(f"शब्दावली: {vectorizer.get_feature_names_out()}\n")

# --- ४. सानो क्लासिफिकेसन पाइपलाइन ---
# थप डेटा (अध्याय १.५ बाट साभार)
documents = [
    ("नेपाल पदयात्राको लागि उत्कृष्ट गन्तव्य हो।", "पर्यटन"),
    ("सगरमाथा आरोहण गर्न विश्वभरबाट पर्यटक आउँछन्।", "पर्यटन"),
    ("नेपालमा जलविद्युत आयोजना निर्माण भइरहेका छन्।", "विकास"),
    ("सडक र पुल निर्माणले ग्रामीण क्षेत्रलाई जोडेको छ।", "विकास"),
    # ... (यहाँ थप डेटा थप्न सकिन्छ)
]

# (नोट: पूर्ण पाइपलाइनको लागि १.५ को कोड सन्दर्भ गर्नुहोस्)
print("४. NLP पाइपलाइन तालिमका लागि तयार छ।")
