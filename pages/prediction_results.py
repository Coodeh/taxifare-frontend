import streamlit as st
import requests

from datetime import datetime, date, time
from zoneinfo import ZoneInfo

from PIL import Image

API_URL = st.secrets['API_BASE_URL']

st.set_page_config(
    page_title="Prediction results",
)

image = Image.open('images/wagon.png')
st.image(image, caption='Le Wagon', use_container_width=False)

st.title(":blue[Prediction results]")
st.write(":green[Here you can see the taxi ride cost based on your inputs].")


# Prediction
if st.button("Predict fare"):

    pickup_date = st.session_state.get("pickup_date", date(2013, 7, 6))
    pickup_time = st.session_state.get("pickup_time", time(17, 0))
    pickup_longitude = st.session_state.get("pickup_longitude", -73.985428)
    pickup_latitude = st.session_state.get("pickup_latitude", 40.748817)
    dropoff_longitude = st.session_state.get("dropoff_longitude", -73.985130)
    dropoff_latitude = st.session_state.get("dropoff_latitude", 40.758896)
    passenger_count = st.session_state.get("passenger_count", 1)

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
