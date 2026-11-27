import io
from tempfile import template

import pandas as pd

import streamlit as st
import requests

from datetime import datetime, date, time
from zoneinfo import ZoneInfo

from PIL import Image

API_BASE_URL = st.secrets['API_BASE_URL']

BATCH_ENDPOINTS = {
    "Linear Regression": "/predict_batch",
    "Random Forest": "/predict_batch_rf",
    "Deep Learning": "/predict_batch_dl"
}

st.set_page_config(
    page_title="Batch predictions",
)

image = Image.open('images/wagon.png')
st.image(image, caption='Le Wagon', use_container_width=False)


st.title(":blue[Batch predictions]")

st.write(
    "Upload a CSV file containing several taxi rides"
)

selected_model = st.selectbox(
    "Choose a model",
    list(BATCH_ENDPOINTS.keys())
)


uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)


if uploaded_file is not None:

    try:

        file_content = uploaded_file.getvalue()

        df = pd.read_csv(
            io.BytesIO(file_content)
        )

        if df.empty:
            st.error("The CSV file is empty.")
            st.stop()

        st.subheader("Uploaded data")

        st.write(
            f"Number of rides: **{len(df)}**"
        )

        st.dataframe(
            df.head(20),
            use_container_width=True
        )

        st.write(
            f"Selected model: **{selected_model}**"
        )

        if st.button(
            "Predict all fares",
            type="primary"
        ):
            endpoint = BATCH_ENDPOINTS[selected_model]
            API_URL = API_BASE_URL + endpoint
            files = {
                "file": (
                    str(uploaded_file.name),
                    uploaded_file.getvalue(),
                    "text/csv"
                )
            }

            try:
                with st.spinner(f"Running:{selected_model}..."):
                    response = requests.post(
                        API_URL,
                        files=files,
                        timeout=120
                    )

                    response.raise_for_status()
                result = pd.read_csv(
                    io.BytesIO(
                        response.content
                    )
                )

                st.success("Batch prediction successful!")

                st.download_button(
                    label="Download predictions",
                    data=result.to_csv(index=False),
                    file_name =("taxifare_predictions.csv"),
                    mime="text/csv",
                    type="primary"
                )
            except requests.exceptions.RequestException as e:

                st.error(f"API error: {e}")

    except requests.exceptions.RequestException as e:

        st.error(f"API error: {e}")
