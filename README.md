# Product Trust & Sentiment Analysis System
This project is designed to scrape product reviews from e-commerce platforms, analyze customer sentiment using NLP techniques, and calculate an overall trustworthiness score for each product.
## Project Setup 
# Open Terminal in VS Code
# Create a Virtual Environment
```bash
python -m venv venv
# Activate the Virtual Environment (Windows)
venv\Scripts\activate

# Install Project Dependencies
pip install -r requirements.txt

## Project Directory Structure
## 📁 data/
Stores all datasets generated during the project.
- raw_reviews.csv – scraped reviews
- processed_reviews.csv – cleaned data
- trust_scores.csv – final trust scores

## 📁 scraper/
Contains scripts for scraping reviews from e-commerce websites.

## 📁 model/
Handles sentiment analysis and trust score calculation.

## 📁 frontend/
Responsible for displaying results in a user-friendly interface.

## Project Purpose
The purpose of this project is to help users evaluate product reliability using real customer feedback.

## Author
Sawera Ashfaq
