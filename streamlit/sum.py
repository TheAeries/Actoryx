import streamlit as st

st.title("Sum of Digits")

num = st.number_input("Enter Number", min_value=0, step=1)

if st.button("Calculate"):
    temp = int(num)
    total = 0

    while temp > 0:
        total += temp % 10
        temp //= 10

    st.success(f"Sum of Digits = {total}")