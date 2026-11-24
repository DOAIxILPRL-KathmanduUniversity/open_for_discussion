polarity_lexicon = {
    "राम्रो": 1, "सफल": 1, "खराब": -1, "समस्या": -1
}
intensifier_lexicon = {
    "एकदमै": 2.0, "अलि": 0.5
}

def analyze_opinion(sentence):
    tokens = sentence.split()
    total_score = 0
    multiplier = 1.0
    for token in tokens:
        if token in intensifier_lexicon:
            multiplier = intensifier_lexicon[token]
        elif token in polarity_lexicon:
            total_score += polarity_lexicon[token] * multiplier
            multiplier = 1.0
    return total_score

if __name__ == "__main__":
    print(f"Score: {analyze_opinion('सरकारको निर्णय एकदमै राम्रो छ।')}")
