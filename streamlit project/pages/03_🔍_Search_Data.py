#Author Sheila Kirwan
#This page contains different Search functionality using streamlit components, html, lists, variables, plotly animated histogram and search functionality, validation
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import plotly.express as px
import datetime as dt
import plotly.io as pio

pageSubTitle = 'Source: Inputted Data file'
st.markdown("<h1 style='text-align: center; color: white;'>Search Event Participant Data</h1>", unsafe_allow_html=True)

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
    st.caption(pageSubTitle)
 
    
    #search fuctionality using text_input functionality and df.loc
    input = st.text_input('Enter the surname of the participant you would like to search For', 'Jones')
    # if input not in df:
    #     st.error("This surname is not available in the inputted file")
    # else:
    df.loc[df['Last Name'] == input ]
    df['Order Timestamp'] = pd.to_datetime(df['Order Timestamp'])  #changing the order timestamp to be correct format
    searchResultName = df.loc[df['Last Name'] == input ] 
    
    @st.cache
    def convert_df(searchResultName):
           # NB The Cache Memorises the function so that resources are not wasted by downloading on every run
        return searchResultName.to_csv().encode('utf-8')

    csv = convert_df(searchResultName)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='name_df.csv',
        mime='text/csv',
    )


    inputDate = st.text_input('Enter an Order Date to see order/s on that date -format required"YYYY-MM-DD"', '2020-01-22')
    df.set_index('Order Timestamp', inplace=True) #changed the index to the order timestamp
    df.loc[df.index == inputDate ] 
    # I would like to add validation so that for both search boxes if not thing is required leave a message
    
    searchResultDate = df.loc[df.index == inputDate ] 

    @st.cache
    def convert_df(searchResultDate):
          # NB The Cache Memorises the function so that resources are not wasted by downloading on every run
        return searchResultDate.to_csv().encode('utf-8')

    csv1 = convert_df(searchResultDate)

    st.download_button(
        label="Download data as CSV",
        data=csv1,
        file_name='date_df.csv',
        mime='text/csv',
    )

    st.markdown("<h2 style='text-align: center; color: white;'>Visualize participant counts by date per County</h2>", unsafe_allow_html=True)
    df['Booking Date'] = pd.to_datetime(df['Booking Date']).dt.strftime("%m/%d/%Y")  #changing the order Booking Date to be specified format
   
    county_choice = df['County'].unique().tolist()
    date_choice = df['Booking Date'].unique().tolist()
    date = st.selectbox('Which date would you like to see participant counts for', date_choice, 100)
    county = st.multiselect('Which county would you like to see participant counts for?', county_choice, ['Dublin'])

    df = df[df['County'].isin(county)]
    # df = df[df['Booking Date']==date] removing the filtering because I'm adding animation

    sumCount = df['Participant Count'].sum()
    st.write(sumCount)


    fig1 = px.histogram(df, x='County', y='Participant Count', color='County',
        range_y=[0,100], animation_frame='Booking Date', animation_group='County') #needed to use a histogram here rather than a bar chart because I needed to aggregate the data.


    fig1.update_layout(width=1500)
    st.write(fig1)









    # st.header ('Plotting orders per date')
    # fig1, ax = plt.subplots(figsize=(12,6), layout='constrained')
    # dates = df.index
    # # data = df['barcode'].value_counts
    # data = np.cumsum(np.random.randn(len(dates)))

  




else:
    st.markdown("<h5 style='text-align: center; color: White;'>Please Upload Your Data File for Analysis</h5>", unsafe_allow_html=True)