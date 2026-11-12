# Password Strength Analyzer

A Python + Streamlit educational application that evaluates user-entered test passwords.

## Features
- Checks password length.
- Checks lowercase, uppercase, digit and special-character complexity.
- Flags a simple repeated-character pattern and a small built-in list of common passwords.
- Displays a strength label and practical improvement suggestions.
- Checks whether a password matches an entry in the app's local password history.
- Optional local SQLite history stores **salted scrypt hashes only**, never plaintext passwords.
- Generates random example passwords with Python's `secrets` module.

## Run the project
1. Install Python 3.9 or newer.
2. Open a terminal in this folder.
3. Create a virtual environment (recommended):
   - Windows: `python -m venv .venv` then `.venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install packages: `pip install -r requirements.txt`
5. Start: `streamlit run app.py`
6. Open the local URL shown in the terminal (usually `http://localhost:8501`).

## How to test
Use fictional examples only:
- `abc` — short and missing character categories.
- `123456` — included in the small common-password examples.
- `mY-random-Test-phrase-482!` — demonstrates a varied passphrase.
- Save a fictional test password to history, then analyze it again to see the reuse warning.

## Project files
- `app.py` — application, analysis functions, password generator and SQLite history.
- `requirements.txt` — Python dependency.
- `PROJECT_NOTES.md` — explanation and viva preparation.

## Security and limitations
This is an educational heuristic, not a professional password-strength estimator. The common-password list is intentionally small and is not a breach database. The SQLite history is local to the machine running the app and is not shared across devices. It stores salted scrypt hashes, not plaintext, but a stolen database can still be attacked offline; do not use this demonstration to store real account passwords. The app asks users to enter fictional test passwords. Password uniqueness is checked only against this app's local history.

## Concepts demonstrated
Python functions, conditionals, loops, strings, regular expressions, secure random generation, SQLite, salted password hashing and basic password-security concepts.

For coursework, review and understand the code, test it yourself, and follow the task provider's rules about acknowledging outside or AI assistance.
