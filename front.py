
# URL de l'API
# api_url = "http://127.0.0.1:8000/"
# 
# # Appel à l'API
# response = requests.get(api_url)
# 
# if response.status_code == 200:
#     st.write(response.json())
# else:
#     st.write("Erreur lors de l'appel à l'API.")
# app.py

import streamlit as st

def add_numbers(num1, num2):
    """Function to add two numbers."""
    return num1 + num2

# Streamlit interface
st.title("Add Two Numbers")
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

if st.button("Add"):
    result = add_numbers(num1, num2)
    st.success(f"The result is: {result}")
