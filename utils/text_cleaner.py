import re

def clean_text(text):
    text = text.lower()                              # all in lowercase
    text = re.sub(r"http\S+", "", text)               # links remove
    text = re.sub(r"[^a-z\s]", "", text)              # special chars remove
    text = re.sub(r"\s+", " ", text).strip()          # remove extra spaces
    return text
