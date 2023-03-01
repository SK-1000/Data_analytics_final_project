

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

    df['Order Timestamp'] = pd.to_datetime(df['Order Timestamp'])  #changing the order timestamp to be correct format
    
    
    

    totalRaised = (df['Raised'].sum())
    formatTotalRaised = "€{:,.2f}".format(totalRaised)
    st.write("The total raised for Charity based on this file data is:")
    st.write(formatTotalRaised)

    st.write("The Maximum amount raised by one person is:")
    maxAmountRaised = df['Raised'].max()
    formatmaxAmountRaised = "€{:,.2f}".format(maxAmountRaised)
    st.write(formatmaxAmountRaised)

    st.write("This Amount was raised by:")
    
    maxAmountRaised1 = df.loc[df['Raised'] == df['Raised'].max(), 'First Name'].unique()
    maxAmountRaised2 = df.loc[df['Raised'] == df['Raised'].max(), 'Last Name'].unique()

    st.write("First Name:")
    st.dataframe(maxAmountRaised1)
    st.write("Last Name:")
    st.dataframe(maxAmountRaised2)
  
    

    st.header('Amount Raised per Charity')
    raisedPerCharityTable = df.pivot_table(index='Charity', values=['Raised'], aggfunc='sum')
    st.dataframe(raisedPerCharityTable)

    st.header('Amount Raised per Charity per Event')
    raisedPerCharityTable = df.pivot_table(index=('Event Name','Charity'), values=['Raised'], aggfunc='sum')
    st.dataframe(raisedPerCharityTable)

    st.header('Amount Raised')
    #The majority of participants are between the ages of approx 35 and 65 with a few outliers
    fig, ax = plt.subplots()
    df['Raised'].plot(kind='box', vert=False, figsize=(14,6))
    st.pyplot(fig)




else:
    st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")