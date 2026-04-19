# grammar_checker.py

import re


def correct_grammar(text):
    """
    Basic grammar correction using rule-based approach.
    """

    if not text or len(text.strip()) == 0:
        return {"error": "Please provide text to check."}

    corrected = text

    # 🔹 Common corrections
    corrections = {
        " i ": " I ",
        "dont": "don't",
        "cant": "can't",
        "wont": "won't",
        "im ": "I'm ",
        "ive ": "I've ",
        "doesnt": "doesn't",
        "isnt": "isn't",
        "didnt": "didn't",
    }

    # Apply word replacements
    for wrong, right in corrections.items():
        corrected = re.sub(r"\b" + re.escape(wrong.strip()) + r"\b", right, corrected, flags=re.IGNORECASE)

    # 🔹 Fix multiple spaces
    corrected = re.sub(r"\s+", " ", corrected)

    # 🔹 Capitalize first letter of sentence
    corrected = corrected.strip()
    if len(corrected) > 0:
        corrected = corrected[0].upper() + corrected[1:]

    # 🔹 Fix spacing before punctuation
    corrected = re.sub(r"\s+([.,!?])", r"\1", corrected)

    # 🔹 Ensure space after punctuation
    corrected = re.sub(r"([.,!?])([A-Za-z])", r"\1 \2", corrected)

    return corrected