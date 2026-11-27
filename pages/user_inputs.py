import streamlit as st
import requests

from datetime import datetime, date, time
from zoneinfo import ZoneInfo

from PIL import Image


st.set_page_config(
    page_title="User inputs",
)


image = Image.open('images/wagon.png')
st.image(image, caption='Le Wagon', use_container_width=False)

st.title(":blue[User inputs]")
st.write(":green[Put your inputs here to predict the taxi ride cost].")


# Date and time
st.subheader(":green[Trip information]")

st.date_input("Pickup date", value=date(2013, 7, 6), key="pickup_date", persist_state="session")

st.time_input("Pickup time", value=time(17, 0), key="pickup_time", persist_state="session")

# Pickup coordinates
st.subheader(":green[Pickup location]")

st.number_input("Pickup longitude", value=-73.985428, format="%.6f", key="pickup_longitude", persist_state="session")

st.number_input("Pickup latitude", value=40.748817, format="%.6f", key="pickup_latitude", persist_state="session")

# Dropoff coordinates
st.subheader(":green[Dropoff location]")

st.number_input("Dropoff longitude", value=-73.985130, format="%.6f", key="dropoff_longitude", persist_state="session")

st.number_input("Dropoff latitude", value=40.758896, format="%.6f", key="dropoff_latitude", persist_state="session")

# Passenger count

st.number_input("Passenger count", min_value=1, max_value=8, value=1, step=1, key="passenger_count", persist_state="session")

if st.button("Save & go to prediction"):
    st.session_state["saved_pickup_date"] = st.session_state["pickup_date"]
    st.session_state["saved_pickup_time"] = st.session_state["pickup_time"]
    st.session_state["saved_pickup_longitude"] = st.session_state["pickup_longitude"]
    st.session_state["saved_pickup_latitude"] = st.session_state["pickup_latitude"]
    st.session_state["saved_dropoff_longitude"] = st.session_state["dropoff_longitude"]
    st.session_state["saved_dropoff_latitude"] = st.session_state["dropoff_latitude"]
    st.session_state["saved_passenger_count"] = st.session_state["passenger_count"]
    st.toast("Inputs saved")
