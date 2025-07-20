import streamlit as st

st.title("Streamlit text input example")
st.write("Enter your name below:")
name = st.text_input("Name", "Type here...")
st.write(f"Hello, {name}!")
st.write("Enter your age below:")
age = st.number_input("Age", min_value=0, max_value=120, value=25)
st.write(f"You are {age} years old.")
st.write("Select your favorite color:")
color = st.selectbox("Color", ["Red", "Green", "Blue"])
st.write(f"Your favorite color is {color}.")


