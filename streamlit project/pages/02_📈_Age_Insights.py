#Author Sheila Kirwan
#This page contains age related pivot tables and charts

from os import truncate
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
import altair as alt
import seaborn as sns
sns.set_theme(style="whitegrid")

df = st.session_state['df']

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



# is file uploaded
if df is not None:
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
    # started with dataframe of Age Category as index and male and female counts for each
    df2 = ageCatPerGenderTable
    
    # created new dataframe with just the first row of the last dataframe
    firstAgeCat = df2.loc[['16-35 Group'],['male','female']]
    df3 = firstAgeCat
    secondAgeCat = df2.loc[['36-56 Group'],['male','female']]
    df4 = secondAgeCat
    thirdAgeCat = df2.loc[['57-77 Group'],['male','female']]
    df5 = thirdAgeCat
    fourthAgeCat = df2.loc[['Masters'],['male','female']]
    df6 = fourthAgeCat
    
    # selected only the values for male and female 
    male = df3.iloc[0,0]
    female = df3.iloc[0,1]
    male4 = df4.iloc[0,0]
    female4 = df4.iloc[0,1]
    male5 = df5.iloc[0,0]
    female5 = df5.iloc[0,1]
    male6 = df6.iloc[0,0]
    female6 = df6.iloc[0,1]
    labels = 'male', 'female'
    sizes = [male, female]
    sizes4 = [male4, female4]
    sizes5 = [male5, female5]
    sizes6 = [male6, female6]


    fig, axs = plt.subplots(2,2)
    axs[0,0].set_title('16-35 Group')
    axs[0,0].pie(sizes, labels = labels, autopct='%1.1f%%')
    axs[0,1].set_title('36-56 Group')
    axs[0,1].pie(sizes4, labels = labels, autopct='%1.1f%%')
    axs[1,0].set_title('57-77 Group')
    axs[1,0].pie(sizes5, labels = labels, autopct='%1.1f%%')
    axs[1,1].set_title('Masters')
    axs[1,1].pie(sizes6, labels = labels, autopct='%1.1f%%')
    st.pyplot(fig)


    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label = 'Average Age', value =df['Age'].mean().round().astype(int))
    with col2:
        st.metric(label = 'Maximum Age', value =df['Age'].max())
    with col3:
        st.metric(label = 'Maximum Age', value =df['Age'].min())



    st.header('Ages Plot Graph')
    #The majority of participants are between the ages of approx 35 and 65 with a few outliers
    fig, ax = plt.subplots()
    df['Age'].plot(kind='box', vert=False, figsize=(14,6))
    st.pyplot(fig)


    st.header('Age Category Per Event')
    ageCatPerEventTable = df.assign(count=1).pivot_table(index='Age Category', columns = 'Event Name', values='count', aggfunc='sum', fill_value=0)
    st.dataframe(ageCatPerEventTable, use_container_width=True)
    st.bar_chart(ageCatPerEventTable)


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

    
    #decided to try using an altair chart from the streamlit documentation description https://docs.streamlit.io/library/api-reference/charts/st.altair_chart
    st.header('Plot of Ticket price paid per age each year')
    c = alt.Chart(df).mark_circle().encode(alt.Y('Event Year', scale=alt.Scale(domain=(2019, 2023))),
    x='Age', size='Ticket Price', color='Ticket Price', tooltip=['Age', 'Event Year', 'Ticket Price'])
    st.altair_chart(c, use_container_width=True)
else:
    # st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")
    st.warning('Please Upload Your Data File for Analysis')
