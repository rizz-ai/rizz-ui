import streamlit as st
import requests
from streamlit_lottie import st_lottie
import numpy as np
import cv2
import validators  
from geosky import geo_plug
import json
from streamlit_extras.no_default_selectbox import selectbox

st.set_page_config(page_title="Rizz.AI", page_icon=":tada:", layout="wide")


countries = geo_plug.all_CountryNames()
raw_states = json.loads(geo_plug.all_Country_StateNames())
statemap={}
for each in raw_states:
    for k,v in each.items():
        statemap[k]=v


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def is_valid_url(url_string: str) -> bool:
    result = validators.url(url_string)
    return result

lottie_coding = load_lottieurl("https://lottie.host/6d6192dd-22e8-4d51-9cd9-75b8c91e34b8/9HFYF0lywc.json")

# Header
with st.container():
    st.subheader("Welcome to Rizz.ai")
    st.title("this is shivali")
    st.write("brand discovery made easy")
    st.write("[Learn More >](https://google.com)")

# Main
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what I do")
        st.write("##")
        st.write('I am shivali')
        st.write("[Learn More >](https://google.com)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("About the brand")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        title = st.text_input('Brand Name')
        street = st.text_input('Street Address')
    with col2:
        website = st.text_input('Website URL')
        if is_valid_url(website)==False:
            st.text("Please enter a valid web url")
        country = selectbox('Country', countries)
    with col3:
         instagram = st.text_input('Instagram Handle')
         if country==None:
             state = st.text_input('State')
         else:
            state = selectbox('State',statemap[country])
    with col4:
        followers = st.number_input('Follower count')
        if state==None:
             city = st.text_input('City')
        else:
            city = selectbox('City',json.loads(geo_plug.all_State_CityNames(state))[0][state] )

    currency = selectbox('Currency', ('USD', 'INR', 'EURO', 'POUND'))
    min_price = st.number_input('Minimum price')
    max_price = st.number_input('Maximum price')

    uploaded_files = st.file_uploader("Upload 5 favorite items from the brand", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            # Convert the file to an opencv image.
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            opencv_image = cv2.imdecode(file_bytes, 1)
            st.write("filename:", uploaded_file.name)
            # Now do something with the image! For example, let's display it:

            st.image(opencv_image, channels="BGR")
            st.write("filename:", uploaded_file.name)

    st.button("Submit")
