import streamlit as st

API_URL = st.secrets['API_BASE_URL']

pg = st.navigation(
    [
        st.Page("pages/model_presentation.py", title="model presentation"),
        st.Page("pages/user_inputs.py", title="user inputs"),
        st.Page("pages/prediction_results.py", title="prediction results"),
        st.Page("pages/batch_prediction.py", title="batch prediction"),

    ]
)
pg.run()
