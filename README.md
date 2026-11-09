# Password Strength Analyzer

A beginner-friendly Python and Streamlit project that evaluates basic password characteristics and gives improvement suggestions.

## Features
- Checks password length.
- Checks lowercase, uppercase, digits, and special characters.
- Flags a simple repeated-character pattern.
- Checks a small built-in list of common passwords.
- Displays an educational strength label and improvement suggestions.
- Generates a random example using Python's `secrets` module.
- Does not intentionally save passwords or send them to an external service.

## Technology
- Python
- Streamlit
- Regular expressions (`re`)
- Python `secrets` module

## Run locally
1. Install Python 3.9 or newer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. (Recommended) Create and activate a virtual environment:

   **Windows**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the application:

   ```bash
   streamlit run app.py
   ```

7. Open the local address printed by Streamlit (usually http://localhost:8501).

## Suggested test inputs
Use made-up examples only; never enter a password you currently use.
- `abc` — short and missing several character categories.
- `123456` — included in the small common-password list.
- `mY-random-Test-phrase-482!` — demonstrates several checklist conditions.

## Project structure
```text
Password-Strength-Analyzer/
├── app.py
├── requirements.txt
└── README.md
```

## Limitations and security notes
This is an educational heuristic, not a professional password-strength estimator. Character variety and length alone cannot prove that a password is secure. The common-password list is small and not comprehensive. The project does not check breached-password databases or implement password-history tracking. Password reuse prevention would require a separate privacy and security design; passwords should never be stored in plaintext.

## Learning concepts
The project demonstrates Python functions, variables, conditionals, loops, strings, regular expressions, Boolean checks, and a simple Streamlit interface.

If this project is used for coursework, review and understand the code, make your own improvements, and follow the course's rules for acknowledging outside or AI assistance.
