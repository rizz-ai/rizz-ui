import json
from http import HTTPStatus

import pandas as pd
import requests
import streamlit as st
from geosky import geo_plug
from streamlit_extras.grid import grid
from streamlit_tags import st_tags

from src import config
from src.utils.currency import CURRENCIES, convert_currency

st.set_page_config(page_title="Brands", page_icon=":shopping_bags:", layout="centered")


def brands():
    st.title("RizzAI")

    countries = sorted(geo_plug.all_CountryNames())
    raw_states: list[dict] = json.loads(geo_plug.all_Country_StateNames())

    states = {k: v for row in raw_states for k, v in row.items()}

    with st.spinner():
        try:
            resp = requests.get(f"{config['api']['url']}/brands").json()

            if resp["status"]["code"] == HTTPStatus.OK:
                brands = pd.DataFrame.from_records(resp["data"]["brands"])
                with st.container():
                    st.subheader("Brands")
                    st.write(brands)
        except:
            st.error("Something went wrong")

    with st.container():
        st.subheader("Add a new brand")

        brand_grid = grid([2, 3])

        brand_name = brand_grid.text_input("Brand Name", help="Enter the brand name")
        url = brand_grid.text_input("Website URL", help="Enter the website URL")

        category = st.multiselect('Category', ["Women's wear", "Men's Wear", "Unisex Brand", "Kids Wear", "Hand Bags", "Accesories", "Footwear", "Other"])
        if 'Other' in category:
            other_category = st_tags(label='Add a custom category:',
            text='Press enter to add more',
            value=[],
            suggestions=[],
            maxtags = 4,
            key='1')

        collection_type = st.multiselect('What is the clothing style of this brand? (Can select multiple)', ['Indian wear', 'Indo-western', 'Western', 'East-Asian', 'African', 'Other'])
        if 'Other' in collection_type:
            other_collection_type = st_tags(label='Add a custom style:',
            text='Press enter to add more',
            value=[],
            suggestions=[],
            maxtags = 4,
            key='1')

        usp = st.text_area("Brand's USP", help="What do you think differentiates this brand from the rest?")

        st.write('---')
        with st.container():
            st.subheader("Contact Information")

            address_grid = grid(1, [3, 2, 2], [1, 2, 3])

            street = address_grid.text_input(
                "Street Address",
                help="Enter the street address without city, state, and country",
                key="street",
                autocomplete="street-address",
            )
            city = address_grid.text_input(
                "City",
                help="Enter the city",
                key="city",
                autocomplete="address-level2",
            )
            country = address_grid.selectbox(
                "Country",
                countries,
                help="Select the country",
                key="country",
            )
            if country:
                state = address_grid.selectbox(
                    "State",
                    sorted(states[country]),
                    help="Select the state",
                    key="state",
                )
            else:
                state = address_grid.selectbox(
                    "State", [], help="Select the country first"
                )
            postal_code = address_grid.text_input(
                "Postal Code",
                help="Enter the postal code",
                key="postal_code",
                autocomplete="postal-code",
            )

            phone = address_grid.text_input(
                "Phone Number",
                help="Enter the phone number",
                key="phone",
                autocomplete="tel",
            )

            email = address_grid.text_input(
                "Email",
                help="Enter the email address",
                key="email",
                autocomplete="email",
            )

    st.write('---')
    with st.container():
        st.subheader("Price Range")

        price_grid = grid(2, 1)

        price_grid.number_input(
            "Minimum Price",
            help="Enter the minimum price in local currency",
            key="min_price",
            value=0,
            step=10,
        )

        price_grid.number_input(
            "Maximum Price",
            help="Enter the maximum price in local currency",
            key="max_price",
            value=0,
            step=10,
        )

        price_grid.selectbox(
            "Currency",
            CURRENCIES,
            help="Select the currency",
            key="currency",
        )
    st.write('---')
    with st.container():
        st.subheader("Socials")

        social_grid = grid([3, 1])

        social_grid.text_input(
            "Instagram Handle",
            help="Enter the Instagram handle",
            key="instagram",
        )

        social_grid.number_input(
            "Follower Count",
            help="Enter the follower count",
            key="follower_count",
            step=1,
        )
    st.write('---')
    with st.container():
        st.subheader("Age")
        start_age, end_age = st.select_slider( 'What age group might this brand appeal to?',options= [x for x in range(0, 100+1) if (x) % 5 == 0],value=(0, 100))
    
    st.write('---')
    with st.container():
        st.subheader("Tags")
        tag_grid = grid([1,1,1],[1,1,1])
        sustainable = tag_grid.checkbox('Sustainable')
        black_owned = tag_grid.checkbox('Black Owned')
        charity = tag_grid.checkbox('Charity/ Support Local')
        celebrity = tag_grid.checkbox('Celeberity Endorsed')
        influencer = tag_grid.checkbox('Influencer Favorite')
        genz = tag_grid.checkbox('Gen-Z Appeal')
        more_tags = st_tags(label='',text='Add more. Type one, hit enter & then type next',
        value=[],
        suggestions=[],
        maxtags = 10,
        key='1')
        size_inclusive = st.multiselect('Is the brand size inclusive or focusses more on clothes for a particular body type?', ['Size Inlcusive', 'Petite', 'Curvy', 'Slim'])

    st.write("---")
    with st.container():
        st.subheader("Occasions")
        st.markdown('''For what occasions/events will you choose outfits from this brand? 
                E.g. winery, date, family dinner, day time events etc. Enter each event separately.''')

        occasion = st_tags(label='',text='Type one event, press enter and then type next',
        value=[],
        suggestions=['winery', 'office', 'date-night', 'date', 'family dinner', 'athletic', 'airport', 'everyday'],
        maxtags = 10,
        key='2')

    st.write("---")
    with st.container():
        st.subheader("Shipping")
        ships_local = st.checkbox('Ships within country')
        if ships_local:
            local_price_grid = grid([1,1,1])

            local_price_grid.selectbox(
                "Currency",
                CURRENCIES,
                help="Select the currency",
                key="local_ship_currency",
            )

            local_price_grid.number_input(
                "Minimum Price",
                help="Enter the minimum price in local currency",
                key="local_ship_min_price",
                value=0,
                step=10,
            )

            local_price_grid.number_input(
                "Maximum Price",
                help="Enter the maximum price in local currency",
                key="local_ship_max_price",
                value=0,
                step=10,
            )

            st.write('---')

        ships_international = st.checkbox('Offers international shipping')
        if ships_international:
            intl_price_grid = grid([1,1,1])

            intl_price_grid.selectbox(
                "Currency",
                CURRENCIES,
                help="Select the currency",
                key="intl_ship_currency",
            )

            intl_price_grid.number_input(
                "Minimum Price",
                help="Enter the minimum price in local currency",
                key="intl_ship_min_price",
                value=0,
                step=10,
            )

            intl_price_grid.number_input(
                "Maximum Price",
                help="Enter the maximum price in local currency",
                key="intl_ship_max_price",
                value=0,
                step=10,
            )

if __name__ == "__main__":
    brands()
