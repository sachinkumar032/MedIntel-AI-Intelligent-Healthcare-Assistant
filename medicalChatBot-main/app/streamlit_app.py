import streamlit as st
from MedQuard import answer_query

st.set_page_config(page_title="MedIntel AI", layout="centered")

st.title("🏥 MedIntel AI")
st.write("Intelligent Healthcare Assistant")

user_input = st.text_input("Ask your medical question:")

if st.button("Get Answer"):
    if user_input:
        response = answer_query(user_input)
        st.success(response)