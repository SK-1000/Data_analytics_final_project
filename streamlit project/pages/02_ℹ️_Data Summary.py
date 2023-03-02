import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import plotly.express as px
import datetime as dt
import plotly.io as pio



#removes the default burger menu
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

uploaded_file = st.sidebar.file_uploader('Upload your file here')
#REMEMBER I CAN CHANGE THE TYPE FOR DATES SO THEY ARE FORMATTED AS DATES SEE CHARITY PAGE FOR EXAMPLE

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
    df['Order Timestamp'] = pd.to_datetime(df['Order Timestamp'])  #changing the order timestamp to be correct format
    
    inputDate = st.text_input('Enter Order Date to see all order on that date (format required'"2020-09-13"'')
    df.set_index('Order Timestamp', inplace=True) #changed the index to the order timestamp
    df.loc[df.index == inputDate ] 
    # I would like to add validation so that for both search boxes if not thing is required leave a message
    
    df['Booking Date'] = pd.to_datetime(df['Booking Date']).dt.strftime("%m/%d/%Y") 
    # df['Booking Date'] = pd.to_datetime(df['Booking Date']).dt.strftime("%d/%m/%Y")  #changing the order Booking Date to be specified format
    county_choice = df['County'].unique().tolist()

    st.write(df)

    
    date_choice = df['Booking Date'].unique().tolist()
    date = st.selectbox('Which date would you like to see', date_choice, 100)
    county = st.multiselect('Which county would you like to see?', county_choice, ['Dublin'])

    df = df[df['County'].isin(county)]
    # df = df[df['Booking Date']==date] removing the filtering because I'm adding animation

    sumCount = df['Participant Count'].sum()
    st.write(sumCount)


    fig1 = px.histogram(df, x='County', y='Participant Count', color='County',
        range_y=[0,100], animation_frame='Booking Date', animation_group='County') #needed to use a histogram here rather than a bar chart because I needed to aggregate the data.


    fig1.update_layout(width=800)
    st.write(fig1)









    # st.header ('Plotting orders per date')
    # fig1, ax = plt.subplots(figsize=(12,6), layout='constrained')
    # dates = df.index
    # # data = df['barcode'].value_counts
    # data = np.cumsum(np.random.randn(len(dates)))

  




else:
    st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")