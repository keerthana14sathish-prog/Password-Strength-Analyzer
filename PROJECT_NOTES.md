# Project Notes and Viva Preparation

## Objective
Develop a tool that evaluates user-entered passwords by checking length, complexity and uniqueness, then suggests ways to improve them.

## Modules
1. **Input and interface:** Streamlit accepts a fictional test password.
2. **Strength analysis:** `analyze_password()` checks length, character types, repeated characters and a small common-password list.
3. **Uniqueness/history:** SQLite stores salted scrypt hashes. A candidate is checked against stored hashes without storing plaintext.
4. **Suggestions:** The app recommends improvements for failed checks.
5. **Password generation:** `secrets` generates a random example.

## Security notes
- Never enter a password used for a real account.
- The database stores salted derived hashes, not plaintext.
- The local database is a learning demonstration, not a production password manager.
- The history only applies to this app's local database and does not synchronize between devices or check breach databases.
- The strength score is a simple heuristic, not a security guarantee.

## Viva questions
**1. What is the purpose?**  
To evaluate basic password characteristics and provide improvement suggestions.

**2. What is password complexity?**  
The use of different character categories, such as uppercase, lowercase, digits and symbols.

**3. What is password uniqueness in this project?**  
The app checks whether a candidate matches a password hash already stored in its local history.

**4. Why use hashing?**  
Hashing transforms a password into a derived value so the original password does not need to be stored.

**5. Why use a salt?**  
A unique random salt makes identical passwords produce different stored hashes and makes precomputed hash attacks harder.

**6. Why use scrypt?**  
Scrypt is a password-based key derivation function designed to make guessing more computationally expensive.

**7. Why use SQLite?**  
SQLite is a lightweight database that stores the local password-history records in a file.

**8. Why use `secrets`?**  
Python's `secrets` module is designed for security-sensitive random values.

**9. Does the score guarantee safety?**  
No. It is an educational checklist. Predictability, uniqueness, length and exposure in breaches also matter.

**10. What is a limitation?**  
The history database is local to one installation and does not synchronize between devices or check breached-password databases.
