from data_scraper.scraper import scrape_reviews
from model.sentiment_model import analyze_sentiments
from model.trust_score import calculate_trust_score

if __name__ == "__main__":
    print("Starting AI Product Trust Analyzer...\n")

    url = input("Enter product URL: ")
    df = scrape_reviews(url)
    if not df.empty:
        analyze_sentiments()
        calculate_trust_score()