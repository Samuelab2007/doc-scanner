import cv2 as cv
from langdetect import detect
import pytesseract

"""
OCR process:
1. Read image
2. Perform basic ocr on most common languages
3. Detect language
4. Rerun ocr only with the detected language
5. Generate pdf output
"""

# lang map to use for tesseractocr
LANG_MAP = {
    "en": "eng",
    "es": "spa",
    "fr": "fra",
    "de": "deu",
    "pt": "por",
    "it": "ita"
}

def detect_language(text_input):
    return detect(text_input)


def perform_ocr(image, output):
    text = pytesseract.image_to_string((image), lang="eng+spa+deu")

    lang = detect_language(text)

    # Maps to language convention used by tesseract. Defaults to "eng" if none are found
    mapped_lang = LANG_MAP.get(lang, "eng")

    doc = pytesseract.image_to_pdf_or_hocr(image, lang=mapped_lang, extension="pdf")

    with open(output, "wb") as f:
        f.write(doc)
    
    print(f"File saved to {output}")

# TODO: Introduce some kind of batch processing. 
