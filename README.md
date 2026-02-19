# Product Trust & Sentiment Analysis System
This project is designed to scrape product reviews from e-commerce platforms, analyze customer sentiment using NLP techniques, and calculate an overall trustworthiness score for each product.
## Project Setup 
# 1. Open Terminal in VS Code
Use the shortcut below to open the terminal:

# 2.Create a Virtual Environment
```bash
python -m venv venv
# 3. Activate the Virtual Environment (Windows)
venv\Scripts\activate
# 4. Install Project Dependencies
pip install -r requirements.txt

Project Directory Structure
📁 data/
This directory stores all datasets generated and used during the project workflow.

raw_reviews.csv
Contains the original scraped customer reviews in raw form.
processed_reviews.csv
Includes cleaned and preprocessed review data (lowercasing, stopword removal, and text normalization).
trust_scores.csv
Final output file containing product-wise trust percentage and sentiment summary.

📁 scraper/
This folder contains Python scripts responsible for scraping review data from e-commerce websites.

scraper.py
Accepts product URLs as input
Uses requests and BeautifulSoup to extract reviews, ratings, and seller details
Saves scraped data into data/raw_reviews.csv

📁 model/
This directory holds the machine learning and natural language processing logic.

sentiment_model.py
Performs sentiment analysis on customer reviews using approaches such as TextBlob or Logistic Regression, classifying reviews as positive, negative, or neutral.
trust_score.py
Calculates an overall trustworthiness score (0–100%) by aggregating sentiment results across all reviews.

📁 frontend/

This folder manages the user interface layer of the application.
Displays sentiment analysis results and trust scores in a clear and user-friendly manner
Fetches processed data from backend logic or CSV outputs
Ensures responsive design for accessibility across multiple devices

Technologies Used
Python
BeautifulSoup & Requests
TextBlob / Machine Learning Models
HTML, CSS, JavaScript
Git & GitHub

Purpose of the Project
The goal of this project is to help users evaluate product reliability by analyzing real customer feedback and generating a transparent trust score based on sentiment analysis.
