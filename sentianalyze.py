import pandas as pd
from textblob import TextBlob

# Load the scraped reviews CSV
df = pd.read_csv("google_play_10_app_reviews.csv")

# Function to calculate sentiment score
def get_sentiment(text):
    try:
        return TextBlob(text).sentiment.polarity
    except:
        return None

# Add sentiment score
df['Sentiment Score'] = df['User Review'].apply(get_sentiment)

# Function to label sentiment
def label_sentiment(score):
    if score is None:
        return 'Unknown'
    elif score > 0.1:
        return 'Positive'
    elif score < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

# Add sentiment label
df['Sentiment Label'] = df['Sentiment Score'].apply(label_sentiment)

# Select only relevant columns
df_clean = df[['App Name', 'User Review', 'Sentiment Score', 'Sentiment Label']]

# Save to CSV
df_clean.to_csv("cleaned_google_play_sentiment.csv", index=False)

# Save to Excel
df_clean.to_excel("cleaned_google_play_sentiment.xlsx", index=False)

print("✅ Sentiment data saved to BOTH CSV and Excel formats.")
