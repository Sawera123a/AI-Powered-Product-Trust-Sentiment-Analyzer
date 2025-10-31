import re

def clean_text(text):
    text = text.lower()                              # sab lowercase me
    text = re.sub(r"http\S+", "", text)               # links remove
    text = re.sub(r"[^a-z\s]", "", text)              # special chars remove
    text = re.sub(r"\s+", " ", text).strip()          # extra spaces hatao
    return text