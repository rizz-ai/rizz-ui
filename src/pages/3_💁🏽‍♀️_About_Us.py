import streamlit as st
from streamlit_lottie import st_lottie

from src.utils.url import load_lottieurl

st.set_page_config(
    page_title="About Us",
    page_icon=":woman_tipping_hand::skin-tone-2:",
    layout="centered",
)


def about():
    st.title("About Us")

    with st.container():
        st.header("Welcome to Rizz.ai")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("What I do")
            st.write("##")
            st.write("I am Shivali")
            st.write("[Learn More >](https://google.com)")

        lottie_coding = load_lottieurl(
            "https://lottie.host/6d6192dd-22e8-4d51-9cd9-75b8c91e34b8/9HFYF0lywc.json"
        )

        with col2:
            if lottie_coding:
                st_lottie(
                    lottie_coding,
                    height=300,
                    key="coding",
                )
        st.divider()


if __name__ == "__main__":
    about()
