import streamlit as st

#creating columns to easily orient objects on the page 
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
  st.write("Welcome to:")
  st.title("*COOKABLE*")
  st.header("Because Googling 'chicken recipe' for the 47th time is exhausting.")

#inserting the image of a dancing chef lottie
#preparing the ground to import the lottie with url
from streamlit_lottie import st_lottie
import requests
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json() 
#actual lottie
lottie_cooking = load_lottie_url("https://lottiefiles.com/free-animation/3d-chef-dancing-NQIgrnDaSK")
st_lottie(lottie_cooking, height=300, key="cooking")


