import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
     characters = string.ascii_letters

     if use_digits:
        characters += string.digits # Adds numbers (0-9) if selected

     if use_special:
        characters += string.punctuation # Adds special characters (!, @, #, $, %, ^, &, *, etc) if selected

     return  ''.join(random.choice(characters) for _ in range(length)) # Generates a random password of the specified length use the selected characters 

st.title("Password Generator")

Length=st.slider("Select Password Length", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Iclude Special Characters")

if st.button("Generate Password"):
    password = generate_password(Length, use_digits, use_special)
    st.write(f"Generated Password:{password}")

st.write("--------------------")

st.write("Build with ❤️ by [MUHAMMAD ADIL AMIR ALI](https://github.com/MUHAMMAD-ADIL-MUHAMMAD-AMIR-ALI)")