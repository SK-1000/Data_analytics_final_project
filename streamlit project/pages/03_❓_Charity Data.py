

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
    st.header('Gender of participants')



    fig9, ax = plt.subplots()  # Create a figure containing a single axes.
    eventName = df["Event Name"]
    gender = df["Gender"].value_counts()
    colors = ["#1f77b4", "#ff7f0e"]
    plt.pie(gender, labels=gender, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=120)
    # plt.title("Gender breakdown\n"+"All Events")
    st.pyplot(fig9)

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