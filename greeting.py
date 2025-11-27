import streamlit as st

# Application Setup
st.title("👋 Interactive Greeting App")
st.markdown("Enter your name below and press the button to receive a personalized greeting.")

# 1. Text input for the user's name
# store the input value in the 'user_name' variable
user_name = st.text_input(
    label="Your Name",
    placeholder="e.g., Alex, Taylor, or Jhon"
)

# 2. Button to trigger the greeting
# check if the button is clicked inside an if statement
if st.button("Greet"):
    # Logic when button is pressed
    
    # Check if the user entered a name
    if user_name:
        # Generate the personalized greeting
        greeting_message = f"Hello, **{user_name}**! Welcome to the interactive world of Streamlit — wishing you an amazing day ahead!"
        
        # Display the greeting using a success box for visibility
        st.success(greeting_message)
        
    else:
        # If the input field was empty
        st.warning("Please enter your name first!")