"""Small, dependency-free Unicode helpers for Persian and Turkish text."""
from .core import (
    normalize_persian,
    search_key,
    to_ascii_digits,
    to_persian_digits,
    turkish_lower,
    turkish_upper,
)

__all__ = [
    "normalize_persian",
    "search_key",
    "to_ascii_digits",
    "to_persian_digits",
    "turkish_lower",
    "turkish_upper",
]
__version__ = "0.1.0"
