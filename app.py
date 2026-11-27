import streamlit as st
import requests

from datetime import datetime, date, time
from zoneinfo import ZoneInfo


API_URL = st.secrets['API_BASE_URL']


st.set_page_config(
    page_title="TaxiFare",
)

st.title("TaxiFare")
st.write("Predict the price of your taxi ride in New York.")


# Date and time
st.subheader("Trip information")

pickup_date = st.date_input(
    "Pickup date",
    value=date(2013, 7, 6)
)

pickup_time = st.time_input(
    "Pickup time (New York)",
    value=time(13, 18)
)


# Pickup coordinates
st.subheader("Pickup location")

pickup_latitude = st.number_input(
    "Pickup latitude",
    value=40.783282,
    format="%.6f"
)

pickup_longitude = st.number_input(
    "Pickup longitude",
    value=-73.950655,
    format="%.6f"
)


# Dropoff coordinates
st.subheader("Dropoff location")

dropoff_latitude = st.number_input(
    "Dropoff latitude",
    value=40.769802,
    format="%.6f"
)

dropoff_longitude = st.number_input(
    "Dropoff longitude",
    value=-73.984365,
    format="%.6f"
)


# Passenger count
passenger_count = st.slider(
    "Passenger count",
    min_value=1,
    max_value=6,
    value=1
)


# Prediction
if st.button("Predict fare"):

    pickup_datetime = datetime.combine(
        pickup_date,
        pickup_time,
        tzinfo=ZoneInfo("America/New_York")
    )

    pickup_datetime_utc = pickup_datetime.astimezone(
        ZoneInfo("UTC")
    )

    params = {
        "pickup_datetime": pickup_datetime_utc.strftime(
            "%Y-%m-%d %H:%M:%S UTC"
        ),
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    try:

        response = requests.get(
            API_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        fare = response.json()["fare"]

        st.success("Prediction successful!")

        st.metric(
            label="Estimated taxi fare",
            value=f"${fare:.2f}"
        )

    except requests.exceptions.RequestException as e:

        st.error(f"API error: {e}")
