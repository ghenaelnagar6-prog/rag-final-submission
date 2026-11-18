import re

with open("raw_book_text.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

print(f"Raw text length: {len(raw_text)} characters")

def clean_text(text):
    text = re.sub(r"--- Page \d+ ---", "", text)
    text = re.sub(r"\n{2,}", "\n", text)
    text = re.sub(r" {2,}", " ", text)
    text = re.sub(r"[.]{3,}", " ", text)
    lines = [line.strip() for line in text.split("\n")]
    lines = [line for line in lines if line != ""]
    return "\n".join(lines)

cleaned_text = clean_text(raw_text)
print(f"Cleaned text length: {len(cleaned_text)} characters")

with open("cleaned_book_text.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print("Saved cleaned_book_text.txt successfully!")
