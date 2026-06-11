import streamlit as st

st.title("Sum of List Elements")

numbers = st.text_input(
    "Enter numbers separated by commas",
    "10,20,30,40"
)

if st.button("Calculate"):
    nums = [int(x) for x in numbers.split(",")]
    st.success(f"Sum = {sum(nums)}")