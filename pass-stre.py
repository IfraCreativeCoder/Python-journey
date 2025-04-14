import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")
st.title("🔐 Password Strength Checker")

st.markdown("""
## Password Strength Checker  
Use this tool to check the strength of your password.
""")

password = st.text_input("Enter your password", type="password")

# Feedback list for suggestions
feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")
        
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password must contain both uppercase and lowercase letters.")
        
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least one digit.")
        
    if re.search(r"[!@#$%^&*(),.?>]", password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least one special character (!@#$%^&*(),.?>).")

    # ✅ Show result based on score
    if score == 4:
        st.success("✅ Your password is strong. 🎊")
    elif score == 3:
        st.warning("⚠️ Your password is medium.")
    else:
        st.error("❌ Your password is weak.")

    # 🔁 Show improvement suggestions
    if feedback:
        st.markdown("### 🔧 Improvement Suggestions:")
        for msg in feedback:
            st.markdown(msg)
else:
    st.info("Please enter a password to check its strength.")

        