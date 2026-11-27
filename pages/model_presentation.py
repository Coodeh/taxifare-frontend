import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Model presentation",
)

image = Image.open('images/wagon.png')
st.image(image, caption='Le Wagon', use_container_width=False)

st.title(":blue[Welcome to the taxi fare model]")

st.subheader(":green[This model is used to predict the price of your taxi ride in New York].")
st.subheader(":orange[Put your predictions in the user inputs page].")
st.subheader(":orange[Visalize the results in the preduction results page].")

st.write(":red[You can also push the button below if you need balloons].")

if st.button('More 🎈🎈🎈 please!'):
    st.balloons()
