import streamlit as st
from PIL import Image

st.set_page_config(page_title="Welcome App", layout="centered")

st.title("Welcome to Streamlit App!")

image = Image.open("image.jpg")
st.image(image, caption="Flowers", use_column_width=True)

st.markdown("""### Hello! 
            Welcome to this simple Streamlit GUI that displays an image and a welcome message. Feel free to explore!""")
