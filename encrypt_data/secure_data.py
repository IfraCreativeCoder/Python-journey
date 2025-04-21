import streamlit as st
import hashlib
from cryptography.fernet import Fernet
import json
import os
import time
from base64 import urlsafe_b64encode
from hashlib import pbkdf2_hmac

# File & security constants
DATA_FILE = "secure_data.json"
SALT = b"secure_salt_value"
LOCKOUT_DURATION = 60  # in seconds

# Session state setup
if "authentication_user" not in st.session_state:
    st.session_state.authentication_user = None

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = 0

# Load user data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Save user data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# Key generation from passphrase
def generate_key(passkey):
    key = pbkdf2_hmac('sha256', passkey.encode(), SALT, 100000)
    return urlsafe_b64encode(key)

# Hash the user password
def hash_password(password):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), SALT, 100000).hex()

# Encrypt and decrypt text using Fernet
def encrypt_text(text, key):
    cipher = Fernet(generate_key(key))
    return cipher.encrypt(text.encode()).decode()

def decrypt_text(encrypted_text, key):
    try:
        cipher = Fernet(generate_key(key))
        return cipher.decrypt(encrypted_text.encode()).decode()
    except:
        return None

# Load existing user data
stored_data = load_data()

# Streamlit UI
st.title("🔐 Secure Data Encryption System")
st.markdown("Safely store and retrieve your encrypted data with a custom passkey. 🧠🔒")

menu = ["🏠 Home", "📝 Register", "🔑 Login", "💾 Store Data", "🔍 Retrieve Data"]
choice = st.sidebar.selectbox("📍 Navigation", menu)

# Home Page
if choice == "🏠 Home":
    st.subheader("👋 Welcome!")
    st.markdown("""
    This system allows you to:
    - Register with a username and password 🧾
    - Securely encrypt and store data using a passkey 🔐
    - Decrypt your data anytime with your passkey 🔍
    - Account locks after 3 failed login attempts for 60 seconds ⏱️
    """)

# Registration Page
elif choice == "📝 Register":
    st.subheader("📋 Register New User")
    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")

    if st.button("Register 🚀"):
        if username and password:
            if username in stored_data:
                st.warning("⚠️ Username already exists.")
            else:
                stored_data[username] = {
                    "password": hash_password(password),
                    "data": []
                }
                save_data(stored_data)
                st.success("✅ User registered successfully!")
        else:
            st.error("❗ Both fields are required.")

# Login Page
elif choice == "🔑 Login":
    st.subheader("🔐 User Login")

    if time.time() < st.session_state.lockout_time:
        remaining = int(st.session_state.lockout_time - time.time())
        st.error(f"⏳ Too many failed attempts. Please wait {remaining} seconds.")
        st.stop()

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login ✅"):
        if username in stored_data and stored_data[username]["password"] == hash_password(password):
            st.session_state.authentication_user = username
            st.session_state.failed_attempts = 0
            st.success(f"🎉 Welcome, {username}!")
        else:
            st.session_state.failed_attempts += 1
            remaining = 3 - st.session_state.failed_attempts
            st.error(f"❌ Invalid credentials! Attempts left: {remaining}")

            if st.session_state.failed_attempts >= 3:
                st.session_state.lockout_time = time.time() + LOCKOUT_DURATION
                st.error("🚫 Too many failed attempts. Locked for 60 seconds.")
                st.stop()

# Store Data Page
elif choice == "💾 Store Data":
    if not st.session_state.authentication_user:
        st.warning("🔐 Please log in first.")
    else:
        st.subheader("📝 Store Encrypted Data")
        data = st.text_area("Enter Data to Encrypt")
        passkey = st.text_input("Encryption Key (Passphrase)", type="password")

        if st.button("Encrypt & Save 💾"):
            if data and passkey:
                encrypted = encrypt_text(data, passkey)
                stored_data[st.session_state.authentication_user]["data"].append(encrypted)
                save_data(stored_data)
                st.success("🔒 Data encrypted and saved successfully!")
            else:
                st.error("❗ All fields are required.")

# Retrieve Data Page
elif choice == "🔍 Retrieve Data":
    if not st.session_state.authentication_user:
        st.warning("🔐 Please log in first.")
    else:
        st.subheader("🔓 Retrieve and Decrypt Data")
        user_data = stored_data.get(st.session_state.authentication_user, {}).get("data", [])

        if not user_data:
            st.info("ℹ️ No data found.")
        else:
            st.write("📜 Encrypted Data Entries:")
            for i, item in enumerate(user_data):
                st.code(item, language="text")

            encrypted_input = st.text_area("Enter Encrypted Text")
            passkey = st.text_input("Enter Passkey to Decrypt", type="password")

            if st.button("Decrypt 🔓"):
                result = decrypt_text(encrypted_input, passkey)
                if result:
                    st.success(f"✅ Decrypted: {result}")
                else:
                    st.error("❌ Incorrect passkey or corrupted data.")
# Footer with inline CSS
st.markdown("""
<hr style='border: 1px solid #999;' />

<div style='text-align: center; padding: 10px; background-color: #0e1117; color: white; border-radius: 10px; font-family: sans-serif; font-size: 14px; margin-top: 20px;'>
    🚀 Secure Data Encryption System | Made with ❤️ by <strong>Ifra Akhter</strong>
</div>
""", unsafe_allow_html=True)