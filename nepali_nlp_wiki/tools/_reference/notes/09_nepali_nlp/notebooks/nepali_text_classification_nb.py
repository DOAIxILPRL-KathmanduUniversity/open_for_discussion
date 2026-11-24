import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# --- 1. DATASET GENERATION ---
data = [
    {'text': 'मलाई दाल भात तरकारी मन पर्छ।', 'label': 'खाना'},
    {'text': 'सगरमाथाको यात्रा अविस्मरणीय थियो।', 'label': 'यात्रा'},
    {'text': 'आजको खाजा म:म हो।', 'label': 'खाना'},
    {'text': 'पोखरा नेपालको सुन्दर शहर हो।', 'label': 'यात्रा'},
    {'text': 'सेल रोटी तिहारको विशेष परिकार हो।', 'label': 'खाना'},
    {'text': 'हामी बसमा चितवन गयौं।', 'label': 'यात्रा'},
    {'text': 'स्याउ स्वास्थ्यको लागि राम्रो फल हो।', 'label': 'खाना'},
    {'text': 'लुम्बिनी गौतम बुद्धको जन्मस्थल हो।', 'label': 'यात्रा'},
    {'text': 'नेवारी खाजा सेट धेरै स्वादिष्ट छ।', 'label': 'खाना'},
    {'text': 'काठमाडौंदेखि पोखराको उडान छोटो थियो।', 'label': 'यात्रा'},
    {'text': 'तातो दूध चिया मेरो रोजाइ हो।', 'label': 'खाना'},
    {'text': 'रारा तालको सुन्दरता बयान गर्न सकिँदैन।', 'label': 'यात्रा'},
    {'text': 'दशैंमा मासुको धेरै परिकार बन्छ।', 'label': 'खाना'},
    {'text': 'गाउँको यात्रा सधैं रमाइलो हुन्छ।', 'label': 'यात्रा'},
    {'text': 'बिहानको नास्तामा रोटी र तरकारी थियो।', 'label': 'खाना'},
    {'text': 'हामीले अन्नपूर्ण आधार शिविरको पदयात्रा गर्यौं।', 'label': 'यात्रा'},
    {'text': 'गुन्द्रुक र ढिंडो नेपालको राष्ट्रिय खाना हो।', 'label': 'खाना'},
    {'text': 'इलामको चिया बगान घुम्न लायक छ।', 'label': 'यात्रा'},
    {'text': 'लसुन र अदुवा मसलाको राजा हुन्।', 'label': 'खाना'},
    {'text': 'पहाडको बाटोमा हिँड्न गाह्रो थियो।', 'label': 'यात्रा'},
    {'text': 'चिसोमा तातो सुप खानुको मज्जै बेग्लै।', 'label': 'खाना'},
    {'text': 'उनले आफ्नो यात्राको अनुभव सुनाए।', 'label': 'यात्रा'},
    {'text': 'केरा एक पौष्टिक फल हो।', 'label': 'खाना'},
    {'text': 'मुस्ताङ जाने बाटोमा स्याउका बगैंचाहरू छन्।', 'label': 'यात्रा'},
    {'text': 'भुटानमा पिरो खाना मन पराउँछन्।', 'label': 'खाना'},
    {'text': 'यात्रा गर्दा नयाँ ठाउँ हेर्न पाइन्छ।', 'label': 'यात्रा'},
    {'text': 'समोसा र चटनी राम्रो खाजा हो।', 'label': 'खाना'},
    {'text': 'आजको उडान समयमै भयो।', 'label': 'यात्रा'},
    {'text': 'माछाको झोल एकदम मिठो थियो।', 'label': 'खाना'},
    {'text': 'विदेश यात्राको लागि भिसा आवश्यक छ।', 'label': 'यात्रा'},
    {'text': 'भर्खरै पकाएको भातको बास्ना राम्रो छ।', 'label': 'खाना'},
    {'text': 'ट्रेकिङ जाँदा पानीको बोतल बोक्नुपर्छ।', 'label': 'यात्रा'},
    {'text': 'दही स्वास्थ्यको लागि लाभदायक छ।', 'label': 'खाना'},
    {'text': 'सौराहमा हात्ती सफारी गर्न सकिन्छ।', 'label': 'यात्रा'},
    {'text': 'यो रेस्टुरेन्टको खाना प्रसिद्ध छ।', 'label': 'खाना'},
    {'text': 'हवाईजहाजबाट हिमाल राम्रो देखिन्छ।', 'label': 'यात्रा'},
    {'text': 'आज डिनरमा के बनाउने?', 'label': 'खाना'},
    {'text': 'लाङटाङ पदयात्रा एक लोकप्रिय विकल्प हो।', 'label': 'यात्रा'},
    {'text': 'गोलभेडा बिना तरकारी अधुरो हुन्छ।', 'label': 'खाना'},
    {'text': 'बसपार्कमा धेरै यात्रुहरू थिए।', 'label': 'यात्रा'}
]
df = pd.DataFrame(data)

# --- 2. TRAIN/TEST SPLIT ---
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42, stratify=df['label'])

# --- 3. VECTORIZATION & MODELING ---
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Smoothing (alpha=1.0) for OOV handling
model = MultinomialNB(alpha=1.0)
model.fit(X_train_vec, y_train)

# --- 4. PREDICTIONS & EVALUATION ---
y_pred = model.predict(X_test_vec)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred):.2%}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# --- 5. VISUALIZATION: WORD CLOUDS ---
font_path = '/usr/local/share/fonts/NotoSansDevanagari-Regular.ttf'

def show_wordcloud(label, color_map):
    corpus = ' '.join(df[df['label'] == label]['text'])
    tokens = re.findall(r'[\u0900-\u097F]+', corpus)
    wc = WordCloud(width=800, height=400, background_color='white', colormap=color_map, font_path=font_path)
    wc.generate_from_frequencies(Counter(tokens))
    plt.figure(figsize=(10, 5))
    plt.imshow(wc)
    plt.title(f"Most Common Words in '{label}' Category")
    plt.axis('off')
    plt.show()

# show_wordcloud('खाना', 'plasma')
# show_wordcloud('यात्रा', 'viridis')
