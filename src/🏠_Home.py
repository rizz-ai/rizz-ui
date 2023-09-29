import streamlit as st

st.set_page_config(page_title="Home", page_icon=":house:", layout="centered")


def home():
    st.balloons()

    st.title("Home")


if __name__ == "__main__":
    home()
