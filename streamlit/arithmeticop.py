import streamlit as st

st.title("Basic Calculator")

num1 = st.number_input("First Number")
num2 = st.number_input("Second Number")

if st.button("Calculate"):
    st.write("Addition:", num1 + num2)
    st.write("Subtraction:", num1 - num2)
    st.write("Multiplication:", num1 * num2)

    if num2 != 0:
        st.write("Division:", num1 / num2)
    else:
        st.error("Cannot divide by zero")