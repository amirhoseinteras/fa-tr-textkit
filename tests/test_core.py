"""Unit tests for stable Persian and Turkish behavior."""
import unittest

from fa_tr_textkit import (
    normalize_persian,
    search_key,
    to_ascii_digits,
    to_persian_digits,
    turkish_lower,
    turkish_upper,
)


class DigitTests(unittest.TestCase):
    def test_ascii_to_persian(self):
        self.assertEqual(to_persian_digits("A1 23"), "A۱ ۲۳")

    def test_arabic_indic_to_persian(self):
        self.assertEqual(to_persian_digits("١٢٣"), "۱۲۳")

    def test_persian_to_ascii(self):
        self.assertEqual(to_ascii_digits("۱۲۳"), "123")

    def test_arabic_indic_to_ascii(self):
        self.assertEqual(to_ascii_digits("٠٩"), "09")

    def test_no_change_to_turkish_letters(self):
        self.assertEqual(to_persian_digits("İstanbul"), "İstanbul")


class PersianTests(unittest.TestCase):
    def test_arabic_kaf_and_yeh(self):
        self.assertEqual(normalize_persian("كتاب فارسي"), "کتاب فارسی")

    def test_zwnj_preserved(self):
        self.assertEqual(normalize_persian("می\u200cروم"), "می\u200cروم")

    def test_digits_ascii(self):
        self.assertEqual(normalize_persian("سال ۱۴۰۵", digits="ascii"), "سال 1405")

    def test_digits_kept(self):
        self.assertEqual(normalize_persian("2026", digits="keep"), "2026")

    def test_invalid_digits(self):
        with self.assertRaises(ValueError):
            normalize_persian("123", digits="latin")

    def test_diacritics_optional(self):
        self.assertEqual(normalize_persian("سَلام", strip_diacritics=True), "سلام")


class TurkishTests(unittest.TestCase):
    def test_lower(self):
        self.assertEqual(turkish_lower("İSTANBUL IŞIK"), "istanbul ışık")

    def test_upper(self):
        self.assertEqual(turkish_upper("istanbul ışık"), "İSTANBUL IŞIK")

    def test_lower_ordinary(self):
        self.assertEqual(turkish_lower("GÜZEL"), "güzel")

    def test_upper_ordinary(self):
        self.assertEqual(turkish_upper("çöğüş"), "ÇÖĞÜŞ")


class SearchTests(unittest.TestCase):
    def test_whitespace_digits_case(self):
        self.assertEqual(search_key("  İSTANBUL   ۱۲۳ "), "istanbul 123")

    def test_variants(self):
        self.assertEqual(search_key("كتاب  كی"), "کتاب کی")

    def test_diacritics(self):
        self.assertEqual(search_key("سَلام"), "سلام")

    def test_preserves_distinct_turkish(self):
        self.assertNotEqual(search_key("SİS"), search_key("SIS"))


if __name__ == "__main__":
    unittest.main()
