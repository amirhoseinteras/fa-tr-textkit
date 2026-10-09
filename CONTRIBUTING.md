# Contributing

Thanks for helping Persian and Turkish text work correctly across tools.

1. Open an issue describing a reproducible Unicode or language edge case.
2. Add a focused test with expected output to `tests/test_core.py`.
3. Implement the minimal fix without adding network calls or sending user text elsewhere.
4. Run `python -m unittest discover -s tests -v` before submitting a pull request.
5. Keep changes substantive and accurately explain what they do. Do not submit mass-generated or duplicative pull requests.

No fabricated download numbers, contributor statistics, stars, or misleading activity claims are permitted. This project is meant to be useful on its own merits.
