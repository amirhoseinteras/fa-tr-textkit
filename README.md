# fa-tr-textkit

[![Automated tests](https://github.com/amirhoseinteras/fa-tr-textkit/actions/workflows/tests.yml/badge.svg)](https://github.com/amirhoseinteras/fa-tr-textkit/actions/workflows/tests.yml)

[GitHub source](https://github.com/amirhoseinteras/fa-tr-textkit) · [Source release](https://github.com/amirhoseinteras/fa-tr-textkit/releases/tag/v0.1.0) · [Report an issue](https://github.com/amirhoseinteras/fa-tr-textkit/issues)

**Install directly from GitHub** (Python 3.9+):

~~~bash
pip install git+https://github.com/amirhoseinteras/fa-tr-textkit.git
~~~

This is a **Python developer library**, not a downloadable Windows desktop EXE. You can download its source ZIP from Releases.


Small, **fully offline**, dependency-free Python helpers for Persian (fa-IR) and Turkish (tr-TR) Unicode text. Useful for bilingual teaching materials, search, captions, and website content.

## Why?

Default Unicode lowercase rules are not always right for Turkish: **I -> ı** and **İ -> i**. Persian text also often mixes Arabic/Persian **ک/ك** and **ی/ي** and three sets of digits. This package addresses these specific problems without sending any text to an API.

## Examples

```python
from fa_tr_textkit import normalize_persian, turkish_lower, turkish_upper, search_key
assert normalize_persian("كتاب فارسي 2026") == "کتاب فارسی ۲۰۲۶"
assert turkish_lower("İSTANBUL IŞIK") == "istanbul ışık"
assert turkish_upper("istanbul ışık") == "İSTANBUL IŞIK"
assert search_key("  İSTANBUL   ۱۲۳ ") == "istanbul 123"
```

### Installation and command line

```bash
pip install -e .
```

```bash
python -m fa_tr_textkit.cli normalize-fa "كتاب فارسي 2026"
python -m fa_tr_textkit.cli lower-tr "İSTANBUL IŞIK"
python -m fa_tr_textkit.cli search-key "  İSTANBUL   ۱۲۳ "
```

After installation (`pip install -e .`), use `fa-tr-textkit` instead of `python -m ...`.

## Persian usage (فارسی)

- تبدیل اعداد انگلیسی و عربی به فارسی یا بالعکس
- اصلاح حروف عربی «ي» و «ك» در متن فارسی
- رعایت نیم‌فاصله (بدون حذف خودکار)
- تبدیل حروف بزرگ و کوچک زبان ترکی با قوانین درست حرف «I/İ»

## Scope and caveats

This is **not** a translator, spell checker, or general transliterator. It preserves Turkish diacritics and deliberately avoids altering punctuation or Persian ZWNJ. Use `search_key()` only when both your indexing and query paths call it consistently.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Contribution guidelines

Bug reports, Unicode edge cases with expected results, documentation examples, and tested features are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE). Created as an original, independent open-source project. No user data, API keys, credentials or website assets are included.
