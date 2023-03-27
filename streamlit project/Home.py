# Author Sheila Kirwan
# This is the home page of my python streamlit app. It contains markdown with html formatting, streamlit components such as st.write and st.sidebar, st.sidebar.fileuploader to name a few.

#

#if the user is logged in and the a file is uploaded then go ahead. If not show warning message


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page

import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import database as db


from PIL import Image
# Loading Image using PIL
im = Image.open('./content/dudeonbike.jfif')


# This widens the space on the page where data is displayed and adds and image and title to the tab
st.set_page_config(layout="wide", page_title="Event Data App", page_icon = im)


# loading the user credentials file
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
# creating an authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'sidebar')


#removes the default hamburger menu
hide_default_format = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_default_format, unsafe_allow_html=True)

if authentication_status:
    authenticator.logout('Logout', 'sidebar')
   

    # hashing passwords for YAML file
    # hashed_passwords = stauth.Hasher(['abc', 'def','ghi']).generate()
    # print(hashed_passwords)

    #These columns allow me to centre the headings and text in the col2
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        # headers, titles and text
        st.markdown("<h1 style='text-align: center; color: White; font-family:system-ui;'>Event Data Analysis Tool</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: White; font-family:system-ui;'>Use current trends to visual further opportunities</h3>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: White; font-family:system-ui;'>Simply input your data and this app will do the rest</h5>", unsafe_allow_html=True)
        st.image('./content/cycle.png',width=500)
    with col3:
        st.write(' ')

    #sidebar code
    with st.sidebar.title('Navigation'):
        st.write(f'Welcome *{name}*')
        uploaded_file = st.sidebar.file_uploader('Upload your file here')

    # is file uploaded
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state['df'] = df
        if username == 'jsmith':
            st.write(f'Welcome *{name}*')     
        elif username == 'rbriggs':
                st.write(f'Welcome *{name}*')          
        elif username == 'skirwan':
                st.write(f'Welcome *{name}*')
  
    else:
        df = st.warning('Please Upload Your Data File for Analysis')
        st.session_state['df'] = df
       # st.markdown("<h5 style='text-align: center; color: White;'>Please Upload Your Data File for Analysis</h5>", unsafe_allow_html=True)
    
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')

