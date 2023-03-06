# Author Sheila Kirwan
# This is the home page of my python streamlit app. It contains markdown with html formatting, streamlit components such as st.write and st.sidebar, st.sidebar.fileuploader to name a few.
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px
import streamlit_authenticator as stauth

from PIL import Image
# Loading Image using PIL
im = Image.open('./content/dudeonbike.jfif')
# This widens the space on the page where data is displayed and adds and image and title to the tab
st.set_page_config(layout="wide", page_title="Event Data App", page_icon = im)

#removes the default hamburger menu
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

#These columns allow me to centre the headings and text in the col2
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    # headers, titles and text
    st.markdown("<h1 style='text-align: center; color: White;'>Event Data Analysis Tool</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: White;'>Use current trends to visual further opportunities</h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: White;'>Simply input your data and this app will do the rest</h5>", unsafe_allow_html=True)
    st.image('./content/cycle.png',width=500)
with col3:
    st.write(' ')

#sidebar code
st.sidebar.title('Navigation')
uploaded_file = st.sidebar.file_uploader('Upload your file here')

# is file uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['df'] = df
else:
    # st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")
    st.markdown("<h5 style='text-align: center; color: White;'>Please Upload Your Data File for Analysis</h5>", unsafe_allow_html=True)
    
