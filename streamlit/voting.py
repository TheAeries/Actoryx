import streamlit as st

st.title("Voting Eligibility Checker")

age = st.number_input("Enter Age", min_value=0, step=1)

if st.button("Check Eligibility"):
    if age >= 18:
        st.success("Eligible to Vote")
    else:
        st.error("Not Eligible to Vote")