from textblob import TextBlob
from deep_translator import GoogleTranslator

def analyze_sentiment(review):
    """
    Detects sentiment from mixed English/Roman Urdu reviews.
    Automatically translates to English if needed.
    Returns: Positive, Negative, or Neutral
    """

    if not review or not isinstance(review, str):
        return "Neutral"

    # Step 1: Clean and prepare text
    text = review.strip()

    try:
        # Step 2: Auto-translate non-English or Roman Urdu text to English
        translator = GoogleTranslator(source='auto', target='en')
        translated_text = translator.translate(text)
    except Exception:
        # Fallback: use original text if translation fails
        translated_text = text

    # Step 3: Analyze sentiment polarity using TextBlob
    blob = TextBlob(translated_text)
    polarity = blob.sentiment.polarity

    # Step 4: Assign sentiment based on polarity score
    if polarity > 0.05:
        sentiment = "Positive"
    elif polarity < -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment


def calculate_trust_score(reviews):
    """
    Calculates trust score based on the proportion of positive reviews.
    Returns: trust_score (float), trust_label (string)
    """

    if not reviews:
        return 0.0, "No Reviews"

    sentiments = [analyze_sentiment(r) for r in reviews]

    positive = sentiments.count("Positive")
    total = len(sentiments)

    trust_score = (positive / total) * 100

    # Weighted logic for small datasets
    if total < 5:
        adjust = -10  # for strict small sample
    elif total > 20:
        adjust = +5   # for large sample
    else:
        adjust = 0

    trust_score = max(0, min(100, trust_score + adjust))

    # Classify product reliability
    if trust_score >= 75:
        label = "✅ Highly Trusted"
    elif trust_score >= 45:
        label = "⚠️ Moderately Trusted"
    else:
        label = "❌ Likely Fraudulent"

    return trust_score, label

# Optional Test Run (you can delete later)
# if __name__ == "__main__":
#     sample_reviews = [
#         "NYC bht pyra tha jasa dikhiya tha bilkul visa he ayea hai 🥰",
#         "quality achi hai par color wo nhi tha jo order Kiya tha",
#         "Material Quality:10/10 fully packed satisfied",
#         "not for same design"
#     ]
#     score, label = calculate_trust_score(sample_reviews)
#     print(f"Trust Score: {score:.2f}% → {label}")