import requests
import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(page_title="Login", page_icon=":lock:", layout="centered")


def login():
    st.title("Login")

    if st.button("Sign Up"):
        pass

    if st.button("Log In"):
        pass


if __name__ == "__main__":
    login()
