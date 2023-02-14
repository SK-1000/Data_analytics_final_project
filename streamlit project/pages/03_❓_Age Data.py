
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
import pandas as pd


uploaded_file = st.sidebar.file_uploader('Upload your file here')


# is file uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['df'] = df

    st.header('Age Category breakdown')



    ageCategoryBreakdown = df['Age Category'].value_counts()       
    st.dataframe(ageCategoryBreakdown)

    fig16, ax = plt.subplots()  # Create a figure containing a single axes.
    df['Age Category'].value_counts().plot(kind='pie', figsize=(6,6) )
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
