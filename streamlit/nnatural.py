import streamlit as st

st.title("First N Natural Numbers")

n = st.number_input("Enter n", min_value=1, step=1)

if st.button("Generate"):
    for i in range(1, n + 1):
        st.write(i)