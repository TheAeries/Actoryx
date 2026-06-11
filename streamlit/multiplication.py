import streamlit as st

st.title("Multiplication Table")

num = st.number_input("Enter Number", step=1)

if st.button("Generate"):
    for i in range(1, 11):
        st.write(f"{num} x {i} = {num*i}")