"""Command line interface; input can be arguments or standard input."""
from __future__ import annotations

import argparse
import sys

from .core import (
    normalize_persian,
    search_key,
    to_ascii_digits,
    to_persian_digits,
    turkish_lower,
    turkish_upper,
)

OPERATIONS = {
    "normalize-fa": normalize_persian,
    "digits-fa": to_persian_digits,
    "digits-ascii": to_ascii_digits,
    "lower-tr": turkish_lower,
    "upper-tr": turkish_upper,
    "search-key": search_key,
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Offline Persian/Turkish Unicode utilities")
    parser.add_argument("operation", choices=OPERATIONS)
    parser.add_argument("text", nargs="*", help="If absent, read from stdin")
    args = parser.parse_args(argv)
    value = " ".join(args.text) if args.text else sys.stdin.read()
    result = OPERATIONS[args.operation](value)
    sys.stdout.write(result)
    if args.text:
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
