import pandas as pd

def calculate_trust_score():
    df = pd.read_csv("data/sentiment_reviews.csv")

    total = len(df)
    if total == 0:
        return 0, "No Data"

    positive = len(df[df["sentiment"] == "Positive"])
    trust_percent = (positive / total) * 100

    if trust_percent >= 70:
        label = "✅ Trusted Product"
    elif trust_percent >= 40:
        label = "⚠️ Be Cautious"
    else:
        label = "❌ Likely Fraudulent"

    print(f"✅ Trust Score: {trust_percent:.2f}% → {label}")
    return trust_percent, label