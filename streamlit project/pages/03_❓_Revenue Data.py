
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl

uploaded_file = st.sidebar.file_uploader('Upload your file here')


# is file uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['df'] = df



    st.header('Ticket Sales per race')

    genderValueTable = df.pivot_table(index='Event Name', values=['Ticket Price', 'Total Price Paid Per Ticket'], aggfunc='sum')
    st.dataframe(genderValueTable)

    st.header('Average Price Paid per ticket')

    fig15, ax = plt.subplots()  # Create a figure containing a single axes.
    AvgPricePerTicketPlot = df['Total Price Paid Per Ticket'].plot(kind='box', vert=False, figsize=(14,6))
    st.pyplot(fig15)

    AvgPricePerTicket = df['Total Price Paid Per Ticket'].describe()
    st.dataframe(AvgPricePerTicket)

    
    st.header('correlation between age year and ticket prices')
    corr =df[['Age','Event Year', 'Ticket Price','Total Price Paid Per Ticket','Ticket Fee','Discount Amount','Additional Purchases Total Paid', 'Raised']].corr()
    st.dataframe(corr)

    st.header('Ticket Price paid per order date')
    st.line_chart(df, x="Order Timestamp", y="Ticket Price")

    fig16 = plt.figure(figsize=(8,8))
    plt.matshow(corr, cmap='RdBu', fignum=fig16.number)
    #need to figure out how to add labels to this correlation chart
    st.pyplot(fig16)







    st.header('Participants sales per gender')

    genderTable = df.pivot_table(index='Gender', aggfunc='sum')
    st.dataframe(genderTable)

    st.header('Participants Ticket sales per gender')

    genderValueTable = df.pivot_table(index='Gender', values=['Ticket Price', 'Total Price Paid Per Ticket'], aggfunc='sum')
    st.dataframe(genderValueTable)

    st.header('Participants Ticket sales per gender per Race')
    genderValuePerEventTable = df.pivot_table(index='Gender', columns='Event Name', values=['Ticket Price', 'Total Price Paid Per Ticket'], aggfunc='sum')
    st.dataframe(genderValuePerEventTable)
else:
    st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")

