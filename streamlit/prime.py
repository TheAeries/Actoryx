import streamlit as st

st.title("Prime Number Checker")

num = st.number_input("Enter Number", min_value=1, step=1)

if st.button("Check"):
    num = int(num)

    if num <= 1:
        st.error("Not Prime")
    else:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            st.success("Prime Number")
        else:
            st.error("Not Prime")