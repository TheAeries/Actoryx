import streamlit as st

st.title("Compare Two Numbers")

num1 = st.number_input("First Number")
num2 = st.number_input("Second Number")

if st.button("Compare"):
    if num1 > num2:
        st.write("First number is greater")
    elif num2 > num1:
        st.write("Second number is greater")
    else:
        st.write("Both numbers are equal")