# Author Sheila Kirwan
#This page contains gender related pivot tables and plots and correllation charts. In some cases here the data is not idea however I wanted to show the possible charts that can be used.
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns

df = st.session_state['df']

pageSubTitle = 'Source: Inputted Data file'
st.markdown("<h1 style='text-align: center; color: white;'>Revenue Insights</h1>", unsafe_allow_html=True)

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
    totalTicketAmountPaid = (df['Total Price Paid Per Ticket'].sum())
    totalTicketAmountPaidEur = "€{:,}".format(round(totalTicketAmountPaid )) # rounded and formatted metrics

    st.metric('Total Combined Ticket Revenue', totalTicketAmountPaidEur)


    st.header('Plot of total Price Paid Per Ticket')
    fig15, ax = plt.subplots()  # Create a figure containing a single axes.
    AvgPricePerTicketPlot = df['Total Price Paid Per Ticket'].plot(kind='box', vert=False, figsize=(14,6))
    st.pyplot(fig15)

    st.header('Ticket Sales per race')
    ticketPricePerRaceTable = df.pivot_table(index='Event Name', values=['Ticket Price', 'Total Price Paid Per Ticket'], aggfunc='sum')
    st.dataframe(ticketPricePerRaceTable)

    st.header('Correlation between age year and ticket prices')
    corr =df[['Age','Event Year', 'Ticket Price','Total Price Paid Per Ticket','Ticket Fee','Discount Amount','Additional Purchases Total Paid', 'Raised']].corr()
    st.dataframe(corr)
    sns.heatmap(corr)
    fig16 = plt.figure(figsize=(8,8))
    plt.matshow(corr, cmap='RdBu', fignum=fig16.number ) #this displays a matrix in a new figure window
    st.pyplot(fig16)

    st.header('Profit per race')
    profitPerRaceTable = df.pivot_table(index='Event Name', values=['Profit Per Ticket'], aggfunc='sum')
    st.dataframe(profitPerRaceTable)

    #REMEMBER I CAN CHANGE THE TYPE FOR DATES SO THEY ARE FORMATTED AS DATES SEE CHARITY PAGE FOR EXAMPLE

    st.header('Ticket Sales per Age Category')
    ticketPricePerAgeTable = df.pivot_table(index='Age Category', values=['Ticket Price', 'Total Price Paid Per Ticket'], aggfunc='sum')
    st.dataframe(ticketPricePerAgeTable)

    st.header('Profit per Age Category')
    profitPerAgeTable = df.pivot_table(index='Age Category', values=['Profit Per Ticket'], aggfunc='sum')
    st.dataframe(profitPerAgeTable)

    st.header('Average Price Paid per ticket')



    st.header('Details of Ticket Prices')
    AvgPricePerTicket = df['Total Price Paid Per Ticket'].describe()
    st.dataframe(AvgPricePerTicket)

    


    st.header('Ticket Price paid per order date')
    st.line_chart(df.head(10), x='Order Timestamp', y='Ticket Price')
    
else:
    st.warning('Please Upload Your Data File for Analysis')