# Author Sheila Kirwan
#This page contains gender related pivot tables and pie charts
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl

df = st.session_state['df']

pageSubTitle = 'Source: Inputted Data file'
st.markdown("<h1 style='text-align: center; color: white;'>Participant Gender Insights</h1>", unsafe_allow_html=True)
st.title('Gender Information')
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
    st.header('Gender of participants in all Races')
    fig9, ax = plt.subplots()  # Create a figure containing a single axes.
    eventName = df["Event Name"]
    gender = df["Gender"].value_counts()
    colors = ["#4BFFC9", "#32a89b"]
    plt.pie(gender, labels=gender, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=120)
    st.pyplot(fig9)

  

    st.header('Participants sales per gender')
    genderTable = df.pivot_table(index='Gender',values=['Ticket Price', 'Total Price Paid Per Ticket'], aggfunc='sum')
    st.dataframe(genderTable)


    st.header('Participant count per Cycle')
    eventGenderTable = df.pivot_table(index='Event Name', values=['Gender'], aggfunc='count')
    st.dataframe(eventGenderTable)


    st.header('Gender Breakdown per Cycle')
    fig10, ax = plt.subplots()  # Create a figure containing a single axes.
    genderBreakPerCycles = df.groupby(['Event Name'])['Gender'].value_counts().plot(kind='pie')
    st.pyplot(fig10)


    st.header('Gender Overview')
    gender1Table = df['Gender'].describe()
    st.dataframe(gender1Table)


    st.header('Participants Ticket sales per gender per Race')
    genderValuePerEventTable = df.pivot_table(index='Gender', columns='Event Name', values=['Ticket Price'], aggfunc='sum')
    st.dataframe(genderValuePerEventTable)


    st.header('Participants Count per gender per Race')
    genderCountPerEventTable = df.assign(count=1).pivot_table(index='Event Name', columns = 'Gender', values='count', aggfunc='sum', fill_value=0)
    # genderCountPerEventTable.plot(kind='bar')
    st.dataframe(genderCountPerEventTable)

    st.header('Participants Count per gender per Annum')
    genderCountPerYearTable = df.assign(count=1).pivot_table(index='Event Year', columns = 'Gender', values='count', aggfunc='sum', fill_value=0)
    st.dataframe(genderCountPerYearTable)
    

else:
    st.warning('Please Upload Your Data File for Analysis')