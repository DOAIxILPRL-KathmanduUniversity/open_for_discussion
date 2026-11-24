"""
🚜 KRISHINET: SOIL HEALTH ANALYSIS
----------------------------------
Cleans and visualizes agricultural field survey data.
Focuses on Soil pH distribution across time and field codes.

Dataset: field survey - Form Responses 1.csv
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_clean_survey(file_path):
    print(f"Loading {file_path}...")
    df = pd.read_csv(file_path)
    
    # 1. Sanitize column names
    df.columns = df.columns.str.strip().str.replace(' ', '_')
    
    # 2. Convert dates
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.sort_values(by='Date', inplace=True)
    
    return df

def plot_soil_ph_stats(df):
    plt.figure(figsize=(12, 5))
    
    # Distribution
    plt.subplot(1, 2, 1)
    sns.histplot(df['soil_ph'], kde=True)
    plt.title('Soil pH Distribution')
    
    # Field comparison
    plt.subplot(1, 2, 2)
    sns.boxplot(x='Field_Code', y='soil_ph', data=df)
    plt.title('Soil pH by Field Code')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # df = load_and_clean_survey('survey.csv')
    # plot_soil_ph_stats(df)
    print("KrishiNet Soil Health Module Ready.")
