"""Deterministic, offline Unicode operations for fa-IR and tr-TR text."""
from __future__ import annotations

import re
import unicodedata

ASCII = "0123456789"
PERSIAN = "۰۱۲۳۴۵۶۷۸۹"
ARABIC_INDIC = "٠١٢٣٤٥٦٧٨٩"
_TO_FA = str.maketrans(ASCII + ARABIC_INDIC, PERSIAN + PERSIAN)
_TO_ASCII = str.maketrans(PERSIAN + ARABIC_INDIC, ASCII + ASCII)
_PERSIAN_VARIANTS = str.maketrans({"ي": "ی", "ى": "ی", "ك": "ک"})
_ARABIC_MARKS = re.compile(r"[\u064b-\u065f\u0670\u06d6-\u06ed]")
_WHITESPACE = re.compile(r"[ \t\r\n\f\v]+")


def to_persian_digits(value: str) -> str:
    """Convert ASCII and Arabic-Indic digits to Persian digits."""
    return value.translate(_TO_FA)


def to_ascii_digits(value: str) -> str:
    """Convert Persian and Arabic-Indic digits to ASCII digits."""
    return value.translate(_TO_ASCII)


def normalize_persian(
    value: str, *, digits: str = "persian", strip_diacritics: bool = False
) -> str:
    """Normalize common Persian/Arabic letter variants without touching ZWNJ.

    digits: 'persian', 'ascii', or 'keep'. This is a conservative normalizer:
    punctuation, diacritics, and half-spaces are preserved unless requested.
    """
    if digits not in ("persian", "ascii", "keep"):
        raise ValueError("digits must be 'persian', 'ascii', or 'keep'")
    value = unicodedata.normalize("NFC", value).translate(_PERSIAN_VARIANTS)
    if strip_diacritics:
        value = _ARABIC_MARKS.sub("", value)
    if digits == "persian":
        value = to_persian_digits(value)
    elif digits == "ascii":
        value = to_ascii_digits(value)
    return value


def turkish_lower(value: str) -> str:
    """Lowercase according to Turkish dotted/dotless-I rules."""
    return value.replace("İ", "i").replace("I", "ı").lower()


def turkish_upper(value: str) -> str:
    """Uppercase according to Turkish dotted/dotless-I rules."""
    return value.replace("i", "İ").replace("ı", "I").upper()


def search_key(value: str) -> str:
    """Create an accent-preserving, case-normalized key for mixed fa/tr search.

    Keeps Turkish distinct letters (ş, ğ, ü, ö, ç) and Persian ZWNJ.
    Normalizes Arabic ya/kaf, converts numbers to ASCII, removes Arabic
    vowel marks and collapses ordinary whitespace.
    """
    value = normalize_persian(value, digits="ascii", strip_diacritics=True)
    value = turkish_lower(value)
    return _WHITESPACE.sub(" ", value).strip()
