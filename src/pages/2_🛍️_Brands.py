import streamlit as st

st.set_page_config(page_title="Brands", page_icon=":shopping_bags:", layout="centered")


def brands():
    st.title("Brands")


if __name__ == "__main__":
    st.sidebar.subheader("Navigation")
