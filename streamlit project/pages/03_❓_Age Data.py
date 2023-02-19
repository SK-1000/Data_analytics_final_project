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

    st.header('Age Category breakdown')
    ageCategoryBreakdown = df['Age Category'].value_counts()       
    st.dataframe(ageCategoryBreakdown)


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
