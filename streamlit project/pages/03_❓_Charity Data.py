

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
   

    totalRaised = (df['Raised'].sum())
    st.write("The total raised for Charity based on this file data is:")
    st.write(totalRaised)


    st.header('Amount Raised per Charity')
    raisedPerCharityTable = df.pivot_table(index='Charity', values=['Raised'], aggfunc='sum')
    st.dataframe(raisedPerCharityTable)

    st.header('Amount Raised per Charity per Event')
    raisedPerCharityTable = df.pivot_table(index=('Event Name','Charity'), values=['Raised'], aggfunc='sum')
    st.dataframe(raisedPerCharityTable)



else:
    st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")