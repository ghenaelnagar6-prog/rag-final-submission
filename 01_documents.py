from pdf2image import convert_from_path
import pytesseract

PDF_PATH = "Injuries and first aid book.pdf"

pages = convert_from_path(PDF_PATH, dpi=200)
print(f"Total pages: {len(pages)}")

extracted_pages = []
for i, page in enumerate(pages):
    text = pytesseract.image_to_string(page, lang="ara")
    extracted_pages.append(text)

with open("raw_book_text.txt", "w", encoding="utf-8") as f:
    for i, text in enumerate(extracted_pages):
        f.write(f"\n--- Page {i+1} ---\n")
        f.write(text)

print("Saved raw_book_text.txt successfully!")
