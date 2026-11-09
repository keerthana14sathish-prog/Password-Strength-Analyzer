# Project Notes and Viva Preparation

## Problem statement
Weak and predictable passwords can put online accounts at risk. This application gives educational feedback about common password characteristics so a user can see areas to improve.

## How the application works
1. The user enters a made-up test password in the Streamlit interface.
2. The `analyze_password()` function checks length and character categories.
3. Regular expressions identify lowercase letters, uppercase letters, digits, symbols, and a simple repeated-character pattern.
4. The application calculates a checklist score and displays a strength label.
5. The application lists suggestions for checks that did not pass.
6. The `generate_example_password()` function demonstrates random generation with Python's `secrets` module.

## Important security decisions
- The app does not intentionally write passwords to files or a database.
- The app does not send passwords to an external API.
- The interface tells users to use made-up test passwords.
- Password reuse tracking is not implemented.
- The displayed score is only a simple educational heuristic.

## Viva questions

**1. What is the purpose of this project?**
To evaluate basic password characteristics and provide suggestions that help users understand password hygiene.

**2. Why is Python used?**
Python has readable syntax and built-in modules for text processing, regular expressions, and secure random generation.

**3. What is Streamlit?**
Streamlit is a Python framework for building interactive web applications with Python.

**4. What is a regular expression?**
A regular expression is a text pattern used to search or match strings. This project uses regular expressions to identify character categories and repeated characters.

**5. Why use `secrets` instead of `random` for password generation?**
The `secrets` module is designed for security-sensitive random values. The `random` module is intended for general-purpose randomness.

**6. Does the score guarantee that a password is secure?**
No. It is a simple educational checklist. Unpredictability, uniqueness, password length, and exposure in data breaches also matter.

**7. Does the application store passwords?**
The application does not intentionally save passwords or send them to an external service. The entered value is processed for the current analysis.

**8. Is password reuse checking included?**
No. It is an optional feature in the task description and is not implemented in this version.

## Before presenting the project
- Run the app locally.
- Test it with made-up strings.
- Understand the functions in `app.py`.
- Be ready to explain the limitations honestly.
- Follow the task provider's rules about acknowledging AI assistance.
