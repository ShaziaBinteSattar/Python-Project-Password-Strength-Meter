import streamlit as st
from pyzxcvbn import zxcvbn  # Use pyzxcvbn instead of zxcvbn

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    result = zxcvbn(password)
    strength_score = result['score']
    feedback = result['feedback']

    st.subheader(f"Password Strength: {strength_score}/4")

    if feedback['warning']:
        st.warning(feedback['warning'])
    
    if feedback['suggestions']:
        st.write("Suggestions:")
        for suggestion in feedback['suggestions']:
            st.write(f"- {suggestion}")
