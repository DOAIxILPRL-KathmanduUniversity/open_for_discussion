"""
🇳🇵 NEPALI CHHANDA ANALYSIS ENGINE
----------------------------------
Detects classical meters (Chhanda) in lyrics line-by-line.
Includes LG (Laghu/Guru) weighting and confidence binning.

Dependencies: pip install pandas seaborn matplotlib
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from chhanda_parser import ChandaParser # Custom module

# --- 1. CONFIGURATION ---
CHANDA_DB_PATH = 'chanda_database.csv'
parser = ChandaParser(CHANDA_DB_PATH)

# --- 2. ANALYSIS LOGIC ---
def analyze_lyrics_line_by_line(lyrics):
    if pd.isna(lyrics): return 'No Chhanda Found', 0.0, None
    
    best_name = 'No Chhanda Found'
    max_conf = 0.0
    best_result = None
    
    for line in lyrics.split('\n'):
        line = line.strip()
        if not line: continue
        
        analysis = parser.analyze(line)
        if analysis and analysis.best_match:
            conf = analysis.best_match.get('similarity', 0.0) * 100
            if conf > max_conf:
                max_conf = conf
                best_name = analysis.best_match.get('name', 'No Chhanda Found')
                best_result = analysis
                
    return best_name, max_conf, best_result

# --- 3. VISUALIZATION HELPERS ---
def plot_confidence_distribution(df):
    bins = [0, 1, 50, 60, 70, 80, 90, 101]
    labels = ['No Match (0%)', '1-49%', '50-59%', '60-69%', '70-79%', '80-89%', '90-100%']
    
    df['confidence_bin'] = pd.cut(df['chhanda_confidence'], bins=bins, labels=labels, right=False)
    
    plt.figure(figsize=(10, 6))
    sns.countplot(x='confidence_bin', data=df, palette='viridis', hue='confidence_bin', legend=False)
    plt.title('Distribution of Chhanda Confidence Bins')
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    # df = pd.read_csv('filtered_ne.csv')
    # df[['best_chhanda', 'chhanda_confidence', 'chhanda_analysis']] = ...
    print("Chhanda Analysis Module Ready.")
