
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl

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


    st.header('Participants Age Category per Annum')
    AgeCatCountPerYearTable = df.assign(count=1).pivot_table(index='Event Year', columns = 'Age Category', values='count', aggfunc='sum', fill_value=0)
    st.dataframe(AgeCatCountPerYearTable)
    
    st.header('Counties by Participant Count')
    AgeCatCountPerYearTable = df.assign(count=1).pivot_table(index='County', values='count', aggfunc='sum', fill_value=0)
    st.dataframe(AgeCatCountPerYearTable)

    st.header('Counties by Participant Count per Age Category')
    AgeCatCountPerYearTable = df.assign(count=1).pivot_table(index='County', columns = 'Age Category', values='count', aggfunc='sum', fill_value=0)
    st.dataframe(AgeCatCountPerYearTable)
else:
    st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")
