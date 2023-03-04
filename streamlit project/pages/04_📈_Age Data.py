#Author Sheila Kirwan
#This page contains age related pivot tables and charts

from os import truncate
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
import altair as alt

pageSubTitle = 'Source: Inputted Data file'
st.markdown("<h1 style='text-align: center; color: white;'>Participant Age Insights</h1>", unsafe_allow_html=True)

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
    st.caption(pageSubTitle)


    #REMEMBER I CAN CHANGE THE TYPE FOR DATES SO THEY ARE FORMATTED AS DATES SEE CHARITY PAGE FOR EXAMPLE
    

    st.header('Age Category breakdown')
    ageCategoryBreakdown = df['Age Category'].value_counts()       
    st.dataframe(ageCategoryBreakdown, use_container_width=True)
    st.bar_chart(ageCategoryBreakdown)

    

    left, right = st.columns(2)
    with right:


        st.header('Age Stats')
        #rounded age stats values with pandas .round function and removed the zeros after the decimal with .astype(int)
        ageStats = df['Age'].describe().round().astype(int)
        st.dataframe(ageStats, use_container_width=True)
  

    with left:
        st.header('Age Category Per Gender')
        ageCatPerGenderTable = df.assign(count=1).pivot_table(index='Age Category', columns = 'Gender', values='count', aggfunc='sum', fill_value=0)
        st.dataframe(ageCatPerGenderTable, use_container_width=True)


    #using matplot lib to plot a pie chart per gender for each Age Category

    df2 = ageCatPerGenderTable
    st.dataframe(df2)

    firstAgeCat = df2.loc[['16-35 Group'],['male','female']]
    df3 = firstAgeCat
    st.dataframe(df3)
    

    male = df3.iloc[0,0]
    st.write(male)
    female = df3.iloc[0,1]
    st.write(female)
    
    labels = 'male', 'female'
    sizes = [male, female]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels = labels, autopct='%1.1f%%')
    st.pyplot(fig)




    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label = 'Average Age', value =df['Age'].mean().round().astype(int))
    with col2:
        st.metric(label = 'Maximum Age', value =df['Age'].max())
    with col3:
        st.metric(label = 'Maximum Age', value =df['Age'].min())



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
