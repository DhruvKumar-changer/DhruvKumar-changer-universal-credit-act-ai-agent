import os
from pathlib import Path

from pypdf import PdfReader


DATA_PATH = Path("data") / "ukpga_20250022_en.pdf"


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
RAW_TEXT_PATH = OUTPUT_DIR / "uc_act_2025_raw.txt"
CLEAN_TEXT_PATH = OUTPUT_DIR / "uc_act_2025_clean.txt"


def extract_raw_text(pdf_path: Path) -> str:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found at {pdf_path}")

    reader = PdfReader(str(pdf_path))
    pages_text = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        # Normalise line breaks
        text = text.replace("\r", "\n")
        pages_text.append(f"[[PAGE {i+1}]]\n{text.strip()}\n")

    return "\n\n".join(pages_text)


def basic_clean(text: str) -> str:
    """
    Light cleaning:
    - remove page markers [[PAGE X]]
    - remove obvious header/footer noise
    - normalise multiple blank lines
    """
    lines = text.splitlines()
    cleaned_lines = []

    for line in lines:
        line = line.strip()

        # skip our own page markers
        if line.startswith("[[PAGE"):
            continue

        # simple header/footer filters (Act title, price line etc. can appear on every page)
        if line.startswith("Universal Credit Act 2025"):
            continue
        if line.startswith("CHAPTER 22"):
            continue
        if line.startswith("? Crown copyright"):
            continue
        if line.startswith("Published by TSO"):
            continue

        if line:
            cleaned_lines.append(line)

    # collapse multiple blank lines
    final_lines = []
    last_blank = False
    for line in cleaned_lines:
        if line == "":
            if not last_blank:
                final_lines.append(line)
            last_blank = True
        else:
            final_lines.append(line)
            last_blank = False

    return "\n".join(final_lines)


def main():
    print(f"Reading PDF from: {DATA_PATH}")
    raw_text = extract_raw_text(DATA_PATH)

    RAW_TEXT_PATH.write_text(raw_text, encoding="utf-8")
    print(f"Saved raw text to: {RAW_TEXT_PATH}")

    clean_text = basic_clean(raw_text)
    CLEAN_TEXT_PATH.write_text(clean_text, encoding="utf-8")
    print(f"Saved clean text to: {CLEAN_TEXT_PATH}")


if __name__ == "__main__":
    main()
