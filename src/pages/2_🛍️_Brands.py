import json
from http import HTTPStatus

import pandas as pd
import requests
import streamlit as st
from geosky import geo_plug
from streamlit_extras.grid import grid

from src import config
from src.utils.currency import CURRENCIES, convert_currency

st.set_page_config(page_title="Brands", page_icon=":shopping_bags:", layout="centered")


def brands():
    st.title("Brands")

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

        brand_name = st.text_input("Brand Name", help="Enter the brand name")

        url = st.text_input("Website URL", help="Enter the website URL")

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


if __name__ == "__main__":
    brands()
