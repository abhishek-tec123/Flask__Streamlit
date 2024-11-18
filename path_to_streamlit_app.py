import streamlit as st

def main():
    # Set the title of the Streamlit app
    st.title("Streamlit App")

    # Add a header
    st.header("Welcome to the Streamlit App!")

    # Add some text
    st.write("This app is integrated with a Flask application and hosted on Render.")

    # Add an input form
    name = st.text_input("What's your name?")
    if st.button("Submit"):
        st.write(f"Hello, {name}! Nice to meet you.")

if __name__ == "__main__":
    main()
