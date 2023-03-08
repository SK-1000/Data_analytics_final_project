import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
import plotly.express as px

df = st.session_state['df']

#removes the default burger menu
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


    
# is file uploaded
if df is not None:

    
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
  
    year_choice = df['Booking Year'].unique().tolist()
    # year = st.selectbox('Select a Year', year_choice, 0) #default is zero
    # df = df[df['Booking Year']==year] # filter the data based on the year


    fig = px.scatter(df, x="Raised", y="Age", size="Profit Per Ticket", color="Event Name", hover_name="Event Name", log_x=True, size_max=55, range_x=[5,10000],
    range_y=[14,110], animation_frame="Booking Year", animation_group="County")

    fig.update_layout(width=800)
    st.write(fig)





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