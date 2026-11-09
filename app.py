import re
import secrets
import string

import streamlit as st

st.set_page_config(page_title="Password Strength Analyzer", page_icon="🔐", layout="centered")

COMMON_PASSWORDS = {
    "password", "password123", "123456", "12345678",
    "qwerty", "admin", "letmein", "welcome", "iloveyou", "abc123",
}


def analyze_password(password: str) -> dict:
    """Check basic password characteristics and return feedback."""
    checks = [
        ("At least 12 characters", len(password) >= 12),
        ("Contains lowercase letters", bool(re.search(r"[a-z]", password))),
        ("Contains uppercase letters", bool(re.search(r"[A-Z]", password))),
        ("Contains numbers", bool(re.search(r"\d", password))),
        ("Contains special characters", bool(re.search(r"[^A-Za-z0-9]", password))),
        ("Avoids a character repeated 3+ times consecutively",
         not bool(re.search(r"(.)\1\1", password))),
    ]

    common = password.lower() in COMMON_PASSWORDS
    score = sum(passed for _, passed in checks)

    if common:
        label, score = "Very weak", 0
    elif score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Moderate"
    elif score == 5:
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
    if common:
        suggestions.append("Avoid common or easily guessed passwords.")
    if not suggestions:
        suggestions.append("Good checklist result. Use a different unique password for every account.")

    return {
        "score": score,
        "label": label,
        "checks": checks,
        "suggestions": suggestions,
        "common": common,
    }


def generate_example_password(length: int = 18) -> str:
    """Generate a random example using Python's security-oriented secrets module."""
    alphabet = string.ascii_letters + string.digits + "!@#$%&*?-_"
    return "".join(secrets.choice(alphabet) for _ in range(length))


st.title("🔐 Password Strength Analyzer")
st.write("Evaluate basic password characteristics and get practical suggestions for improvement.")
st.info(
    "Privacy notice: this demo analyzes the entered value in the current app session. "
    "It does not intentionally save passwords or send them to an external service. "
    "For testing, enter a made-up password—not a password you use for an account."
)

with st.form("analyzer_form"):
    password = st.text_input("Enter a test password", type="password")
    submitted = st.form_submit_button("Analyze password", type="primary")

if submitted:
    if not password:
        st.warning("Please enter a test password.")
    else:
        result = analyze_password(password)
        st.subheader("Analysis result")
        st.metric("Estimated strength", result["label"])
        st.progress(result["score"] / 6)
        st.caption(
            f"Checklist score: {result['score']} / 6. "
            "This simple educational score is not a guarantee of security."
        )
        st.subheader("Security checklist")
        for check_name, passed in result["checks"]:
            st.write(f"{'✅' if passed else '❌'} {check_name}")
        st.subheader("Suggestions")
        for suggestion in result["suggestions"]:
            st.write(f"• {suggestion}")

st.divider()
st.subheader("Generate a random example")
st.write("Uses Python's secrets module to generate a random example locally.")
if st.button("Generate example password"):
    st.code(generate_example_password())
    st.caption("This is an example for learning. Use a reputable password manager for real accounts.")

st.caption(
    "Educational project. The common-password list is intentionally small; "
    "this tool is not a full password audit or breach checker."
)
