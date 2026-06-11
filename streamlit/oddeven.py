import streamlit as st

st.title("Even or Odd Checker")

num = st.number_input("Enter an integer", step=1)

if st.button("Check"):
    if num % 2 == 0:
        st.success("Even Number")
    else:
        st.success("Odd Number")