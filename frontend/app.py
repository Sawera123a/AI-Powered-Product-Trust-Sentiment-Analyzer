import sys
import os
import streamlit as st

# Add parent directory to path (for model imports)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_scraper.scraper import scrape_reviews
from model.sentiment_model import calculate_trust_score

# Page setup
st.set_page_config(page_title="Daraz Product Trust Analyzer", page_icon="🛒", layout="centered")
st.title("🛍️ Daraz Product Trust & Sentiment Analyzer")

# Input field
url = st.text_input("🔗 Paste Daraz Product Link:")

# Button click
if st.button("Analyze"):
    if not url.strip():
        st.warning("⚠️ Please paste a valid Daraz product link!")
    else:
        # 🕓 Use spinner while scraping
        with st.spinner("🔍 Scraping in progress... Please wait 10–15 seconds."):
            result = scrape_reviews(url)

        # ✅ Handle results
        if "error" in result:
            st.error(result["error"])
        else:
            st.success(f"✅ Product: {result['product_name']}")
            st.write(f"⭐ **Average Rating:** {result['avg_rating']}")
            st.write(f"💯 **Trust Score (Site Data):** {result['trust_score']}%")
            st.write(f"📝 **Total Reviews:** {result['total_reviews']}")

            # 🗂️ Show sample reviews
            if result["total_reviews"] > 0:
                with st.expander("🗂️ Show Sample Reviews"):
                    for rev in result["reviews"][:5]:
                        st.write(f"- {rev}")
            else:
                st.warning("No reviews found for this product.")

            # 🧠 AI Sentiment Analysis Section
            with st.spinner("🧠 Running AI Sentiment Analysis..."):
                try:
                    trust_percent, label = calculate_trust_score(result["reviews"])
                    st.success(f"{label} ({trust_percent:.2f}% Positive Reviews)")
                except Exception as e:
                    st.error(f"⚠️ Sentiment analysis failed: {e}")