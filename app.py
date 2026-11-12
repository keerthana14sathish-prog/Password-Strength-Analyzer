import hashlib
import hmac
import re
import secrets
import sqlite3
import string
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Password Strength Analyzer", page_icon="🔐", layout="centered")

DB_PATH = Path(__file__).with_name("password_history.db")
COMMON_PASSWORDS = {
    "password", "password123", "123456", "12345678",
    "qwerty", "admin", "letmein", "welcome", "iloveyou", "abc123",
}


def initialize_database():
    """Create a local table for salted password hashes; never store plaintext passwords."""
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS password_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                salt BLOB NOT NULL,
                password_hash BLOB NOT NULL
            )
        """)


def hash_password(password, salt=None):
    """Derive a slow salted hash for local password-history comparison."""
    salt = salt or secrets.token_bytes(16)
    digest = hashlib.scrypt(
        password.encode("utf-8"), salt=salt, n=2**14, r=8, p=1, dklen=32
    )
    return salt, digest


def was_used_before(password):
    """Compare a candidate against saved salted hashes without storing plaintext."""
    initialize_database()
    with sqlite3.connect(DB_PATH) as connection:
        records = connection.execute(
            "SELECT salt, password_hash FROM password_history"
        ).fetchall()
    for salt, saved_hash in records:
        _, candidate_hash = hash_password(password, salt)
        if hmac.compare_digest(candidate_hash, saved_hash):
            return True
    return False


def save_password_hash(password):
    """Save only a salted derived hash in the local history database."""
    salt, digest = hash_password(password)
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            "INSERT INTO password_history (salt, password_hash) VALUES (?, ?)",
            (salt, digest),
        )


def analyze_password(password):
    """Evaluate length, character variety, common patterns and repetition."""
    checks = [
        ("At least 12 characters", len(password) >= 12),
        ("Contains lowercase letters", bool(re.search(r"[a-z]", password))),
        ("Contains uppercase letters", bool(re.search(r"[A-Z]", password))),
        ("Contains numbers", bool(re.search(r"\d", password))),
        ("Contains special characters", bool(re.search(r"[^A-Za-z0-9]", password))),
        ("Does not repeat one character 3+ times consecutively",
         not bool(re.search(r"(.)\1\1", password))),
        ("Not in the built-in common-password examples",
         password.lower() not in COMMON_PASSWORDS),
    ]
    score = sum(passed for _, passed in checks)
    if score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Moderate"
    elif score <= 6:
        label = "Strong"
    else:
        label = "Very strong"

    suggestions = []
    if len(password) < 12:
        suggestions.append("Use a longer passphrase (12–16+ characters is a useful target).")
    if not re.search(r"[a-z]", password):
        suggestions.append("Include lowercase letters.")
    if not re.search(r"[A-Z]", password):
        suggestions.append("Include uppercase letters.")
    if not re.search(r"\d", password):
        suggestions.append("Include numbers.")
    if not re.search(r"[^A-Za-z0-9]", password):
        suggestions.append("Consider including a symbol.")
    if re.search(r"(.)\1\1", password):
        suggestions.append("Avoid repeating the same character several times.")
    if password.lower() in COMMON_PASSWORDS:
        suggestions.append("Avoid common or easily guessed passwords.")
    if not suggestions:
        suggestions.append("Good checklist result. Use a unique password for every account.")
    return {"score": score, "label": label, "checks": checks, "suggestions": suggestions}


def generate_password(length=18):
    """Generate an example using Python's security-oriented secrets module."""
    alphabet = string.ascii_letters + string.digits + "!@#$%&*?-_"
    return "".join(secrets.choice(alphabet) for _ in range(length))


initialize_database()
st.title("🔐 Password Strength Analyzer")
st.write("Evaluate password length, complexity and uniqueness, and get suggestions for improvement.")
st.info(
    "Privacy: this demo keeps a local password-history database containing salted password hashes, "
    "not plaintext passwords. Use fictional test passwords only. Do not enter a password you use for a real account."
)

password = st.text_input("Enter a test password", type="password")

if st.button("Analyze password", type="primary"):
    if not password:
        st.warning("Please enter a test password.")
    else:
        result = analyze_password(password)
        previously_used = was_used_before(password)
        st.subheader("Analysis result")
        if previously_used:
            st.error("This password appears in this application's saved history. Choose a different password.")
        else:
            st.metric("Estimated strength", result["label"])
        st.progress(result["score"] / 7)
        st.caption(
            f"Checklist score: {result['score']} / 7. This educational score is not a guarantee of security."
        )
        st.subheader("Security checklist")
        for name, passed in result["checks"]:
            st.write(f"{'✅' if passed else '❌'} {name}")
        st.write("**Password uniqueness:** " + ("❌ Previously used in this local history." if previously_used else "✅ Not found in this local history."))
        st.subheader("Suggestions")
        for item in result["suggestions"]:
            st.write("• " + item)
        if not previously_used:
            if st.button("Save this password to local history (hash only)"):
                save_password_hash(password)
                st.success("A salted hash was saved. The original password was not stored.")

st.divider()
st.subheader("Generate a stronger example")
if st.button("Generate random example password"):
    st.code(generate_password())
    st.caption("Generated locally with Python's secrets module. Use a password manager for real accounts.")

st.caption(
    "Educational project only. The built-in common-password list is small. "
    "The local history database is for demonstration and is not synchronized across devices."
)
