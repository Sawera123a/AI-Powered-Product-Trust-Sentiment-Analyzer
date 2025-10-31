VS Code me terminal open karo (shortcut: Ctrl + ~)
Virtual environment banana chahe to banao:
->python -m venv venv
->Activate karo:
venv\Scripts\activate   # (Windows)

Dependencies install karo:
pip install -r requirements.txt

data/:
Meaning: yah folder tumhare saare data files rakhta hai —
jo tum scrape karte ho, clean karte ho, ya output generate karte ho.
raw_reviews.csv → original scraped data (raw form).
processed_reviews.csv → cleaned data (stopwords remove, lowercase, etc).
trust_scores.csv → final file jisme har product ka trust % aur sentiment summary hogi.

scraper/:
Meaning: ye folder un Python scripts ke liye hai jo websites (like Daraz, Amazon) se data nikalte hain.
scraper.py — main script jo:
product link input le ga,
BeautifulSoup + requests se reviews, ratings aur seller info extract karega,
aur output data/raw_reviews.csv me save karega.

model/:
Meaning: yah tumhare AI/ML code ke liye folder hai —
sentiment analysis aur trust calculation yahan hoti hai.
sentiment_model.py
TextBlob / Logistic Regression ka use karke har review ka positive, negative, neutral score nikalta hai.
trust_score.py
sab reviews ka overall trustworthiness percentage (0–100%) calculate karta hai.

frontend/

Meaning: yah folder Streamlit app ke liye hai jahan user product link paste karega
aur AI ke results dekhega — sentiment graph, trust score, aur recommendation.
app.py
ek simple dashboard banata hai
product link input field deta hai
result me “Trusted Product ✅” / “Be Cautious ⚠️” / “Likely Fraudulent ❌” show karta hai.


venv\Scripts\activate   # (Windows)
then,

streamlit run frontend/app.py