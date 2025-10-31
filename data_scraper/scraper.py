import time
import os
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scrape_reviews(url):
    data = {}

    try:
        # Chrome setup (headless browser)
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/118.0.0.0 Safari/537.36")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        driver.get(url)
        time.sleep(10)  # Wait for reviews to load

        # Product name
        try:
            product_name = driver.find_element(By.TAG_NAME, "h1").text.strip()
        except:
            product_name = "Unknown Product"

        # Ratings extraction (stars)
        try:
            rating_element = driver.find_element(By.CSS_SELECTOR, "span.score-average")
            avg_rating = float(rating_element.text.strip())
        except:
            avg_rating = 0.0

        # Review texts
        review_elements = driver.find_elements(By.CSS_SELECTOR, ".content")
        reviews = [r.text.strip() for r in review_elements if r.text.strip()]

        total_reviews = len(reviews)

        # Calculate trust score (simple weighted logic)
        trust_score = round((avg_rating / 5) * 100, 2) if avg_rating > 0 else 0.0

        # Save data
        data = {
            "product_name": product_name,
            "avg_rating": avg_rating,
            "trust_score": trust_score,
            "total_reviews": total_reviews,
            "reviews": reviews
        }

        df = pd.DataFrame([data])
        df.to_csv("data/processed_reviews.csv", index=False)

        # Also save summary to trust_scores.csv (append history)
        df_summary = pd.DataFrame([{
            "Product Name": product_name,
            "Average Rating": avg_rating,
            "Trust Score (%)": trust_score,
            "Total Reviews": total_reviews
        }])
        df_summary.to_csv("data/trust_scores.csv", mode='a', index=False, header=not os.path.exists("data/trust_scores.csv"))

        driver.quit()

    except Exception as e:
        data = {"error": f"Scraping failed: {str(e)}"}

    return data