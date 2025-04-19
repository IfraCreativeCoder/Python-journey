import streamlit as st 

# --- Add custom CSS ---
st.markdown("""
    <style>
        div.stButton > button {
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# --- App Title & Description ---
st.title("🌎 Unit Converter App")
st.markdown("### Converts Length, Weight, And Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

# --- Conversion Function ---
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
    return None

# --- Session State for Result ---
if "result" not in st.session_state:
    st.session_state.result = ""

# --- User Inputs ---
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

if category == "Length":
    unit = st.selectbox("Select conversion", ["Miles to Kilometers", "Kilometers to Miles"])
elif category == "Weight":
    unit = st.selectbox("Select conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("Select conversion", [
        "Seconds to Minutes", "Minutes to Seconds", 
        "Minutes to Hours", "Hours to Minutes", 
        "Hours to Days", "Days to Hours"
    ])

value = st.number_input("Enter the value to convert", min_value=0.0, format="%.2f")

# --- Convert Button ---
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.session_state.result = f"The result is {result:.2f}"
    else:
        st.session_state.result = "Invalid conversion. Please try again."

# --- Display Result ---
if st.session_state.result:
    if "Invalid" in st.session_state.result:
        st.error(st.session_state.result)
    else:
        st.success(st.session_state.result)

