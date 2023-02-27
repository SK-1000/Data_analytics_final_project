import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#removes the default burger menu
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

uploaded_file = st.sidebar.file_uploader('Upload your file here')


# is file uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['df'] = df
    #creating new dataframe that drops any column with N/A
    df2=df.drop(["Public health measures for COVID-19", "I have read  and agree to abide by the above Public health measures for COVID-19",
         " understand", " and agree to abide by the above Public health measures for COVID-19", "Privacy Policy", "Refund and Transfer Policy", 
         "Cycling Ireland Licence Number", "Club", "Rider Category", 'UCI ID', 'Date of Purchase', 'Active Order Number', 'Active CI Member', 'Active CI Number',
         'Active County', 'Active Mobile', 'Comment', 'Fundraiser Status'], axis = 1)
    st.header('Data Statistics')
    st.write(df2.describe())


    #search fuctionality using text_input functionality and df.loc
    input = st.text_input('Enter the surname of the participant you would like to search For')
    df.loc[df['Last Name'] == input ] 
    

else:
    st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")