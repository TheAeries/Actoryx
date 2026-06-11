import streamlit as st

st.title("Positive / Negative / Zero")

num = st.number_input("Enter Number")

if st.button("Check"):
    if num > 0:
        st.success("Positive Number")
    elif num < 0:
        st.error("Negative Number")
    else:
        st.info("Zero")