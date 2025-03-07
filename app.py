import streamlit as st
import re

# 🚀 App Title
st.title("🔒 Secure Password Analyzer")

# ℹ️ Description
st.markdown(
    """
    Strengthen your security with our **Password Strength Checker**!
    
    🔍 This tool evaluates passwords based on:
    - ✅ Minimum Length (8+ characters)
    - ✅ Upper & Lowercase Letters
    - ✅ Numeric Digits
    - ✅ Special Characters (!@#$%^&*)
    
    ⚡ *Enhance your online protection now!*
    """
)

# 🏷️ Password Input
password = st.text_input("🔑 Enter your password:", type="password")

# 🔎 Function to Analyze Password Strength
def analyze_password(password):
    score = 0
    issues = []

    if len(password) >= 8:
        score += 1
    else:
        issues.append("🔸 Use at least **8 characters**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        issues.append("🔸 Include **both uppercase & lowercase letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        issues.append("🔸 Add at least **one number** (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        issues.append("🔸 Use at least **one special character** (!@#$%^&*).")

    return score, issues

# 🎯 Check Password Button
if st.button("🔍 Analyze Password"):
    if password:
        strength, suggestions = analyze_password(password)

        st.subheader("🔐 Password Strength Report:")
        if strength == 4:
            st.success("✅ Strong Password! Your credentials are secure.")
        elif strength == 3:
            st.warning("⚠️ Fair Password - Improve security by following suggestions below.")
        else:
            st.error("❌ Weak Password - Consider making it stronger.")

        if suggestions:
            st.info("💡 Ways to Strengthen Your Password:")
            for tip in suggestions:
                st.write(tip)
    else:
        st.error("🚨 Please input a password to evaluate.")


