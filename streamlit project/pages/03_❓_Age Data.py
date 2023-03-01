from os import truncate
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
import altair as alt



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


    #REMEMBER I CAN CHANGE THE TYPE FOR DATES SO THEY ARE FORMATTED AS DATES SEE CHARITY PAGE FOR EXAMPLE

    
    st.header('Age Category breakdown')
    ageCategoryBreakdown = df['Age Category'].value_counts()       
    st.dataframe(ageCategoryBreakdown)
    st.bar_chart(ageCategoryBreakdown)


    st.header('Age Stats')
    #rounded age stats values with pandas .round function and removed the zeros after the decimal with .astype(int)
    ageStats = df['Age'].describe().round().astype(int)
    st.dataframe(ageStats)
  
    st.header('Age Category Per Gender')
    ageCatPerGenderTable = df.assign(count=1).pivot_table(index='Age Category', columns = 'Gender', values='count', aggfunc='sum', fill_value=0)
    st.dataframe(ageCatPerGenderTable)

    
    st.header('Ages')
    #The majority of participants are between the ages of approx 35 and 65 with a few outliers
    fig, ax = plt.subplots()
    df['Age'].plot(kind='box', vert=False, figsize=(14,6))
    st.pyplot(fig)



    

    st.header('Age Category Per Event')
    ageCatPerEventTable = df.assign(count=1).pivot_table(index='Age Category', columns = 'Event Name', values='count', aggfunc='sum', fill_value=0)
    st.dataframe(ageCatPerEventTable)



    st.header('Participants Age Category per Annum')
    AgeCatCountPerYearTable = df.assign(count=1).pivot_table(index='Event Year', columns = 'Age Category', values='count', aggfunc='sum', fill_value=0)
    st.dataframe(AgeCatCountPerYearTable)


    st.header('Participants Age Category per Race Distance')
    AgeCatCountPerDistTable = df.assign(count=1).pivot_table(index='TicketType', columns = 'Age Category', values='count', aggfunc='sum', fill_value=0)
    st.dataframe(AgeCatCountPerDistTable)

    st.header ('Age Category Profit')
    ax = df[['Profit Per Ticket', 'Age Category']].boxplot(by='Age Category',figsize=(10,6))
    ax.set_ylabel('Profit')

    fig16, ax = plt.subplots()  # Create a figure containing a single axes.
    df['Age Category'].value_counts().plot(kind='pie', figsize=(6,6) )
    st.pyplot(fig16)

    

    fig17, ax = plt.subplots(1,1)
    ax.scatter(x=df['Event Year'], y=df['Age'])
    ax.set_xlabel=('Event Year')
    st.pyplot(fig17)


    
    #decided to try using an altair chart from the streamlit documentation description https://docs.streamlit.io/library/api-reference/charts/st.altair_chart
    st.header('Plot of Ticket price paid per age each year')
    c = alt.Chart(df).mark_circle().encode(alt.Y('Event Year', scale=alt.Scale(domain=(2019, 2023))),
    x='Age', size='Ticket Price', color='Ticket Price', tooltip=['Age', 'Event Year', 'Ticket Price'])
    st.altair_chart(c, use_container_width=True)
else:
    st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")
