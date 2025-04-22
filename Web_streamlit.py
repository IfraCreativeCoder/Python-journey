import streamlit as st

# Page Configuration
st.set_page_config(page_title="My Webpage", page_icon="🎉", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stTextInput > div > div > input,
    .stTextArea > div > textarea {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #d3d3d3;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.subheader("Hi, I am Ifra 👋")
st.title("🐍 A Python Programmer")
st.write("💡 I am passionate about finding ways to use Python to be more efficient and effective in business settings.")
st.write("[🚀 Visit My GitHub](https://github.com/IfraCreativeCoder/python-journey)")

# What I Do Section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("💻 What I Do")
        st.write("##")
        st.write("""
        🧠 I am currently sharpening my Python skills and building awesome projects!  
        🎮 Games I've made:  
        - Hangman  
        - Guess the Number  
        - Mad Libs  
        - Rock Paper Scissors  
        - Countdown Timer  
        - BMI Calculator  
        
        🚀 My mission is to level up my programming game with fun and impactful projects!
        """)

# Contact Section
with st.container():
    st.write("---")
    st.header("📬 Get In Touch With Me!")
    st.write("##")

    left_column, right_column = st.columns(2)

    with left_column:
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("👤 Your Name")
            message = st.text_area("✍️ Your Feedback Here")
            submitted = st.form_submit_button("📨 Send Message")
            if submitted:
                st.success("🎉 Your feedback has been submitted!")

    with right_column:
        st.image("https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif", width=300)

