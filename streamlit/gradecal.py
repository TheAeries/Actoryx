import streamlit as st

st.title("Student Grade Calculator")

name = st.text_input("Student Name")

maths = st.number_input("Maths Marks", 0, 100)
physics = st.number_input("Physics Marks", 0, 100)
chemistry = st.number_input("Chemistry Marks", 0, 100)

if st.button("Calculate Grade"):
    total = maths + physics + chemistry

    if total >= 270:
        grade = "A"
    elif total >= 240:
        grade = "B"
    elif total >= 180:
        grade = "C"
    else:
        grade = "D"

    st.write("Name:", name)
    st.write("Total:", total)
    st.success(f"Grade: {grade}")