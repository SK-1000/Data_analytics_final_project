
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl

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

    st.header('Gender of participants in all Races')
    fig9, ax = plt.subplots()  # Create a figure containing a single axes.
    eventName = df["Event Name"]
    gender = df["Gender"].value_counts()
    colors = ["#4BFFC9", "#32a89b"]
    plt.pie(gender, labels=gender, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=120)
    # plt.title("Gender breakdown\n"+"All Events")
    st.pyplot(fig9)

    # st.header('Gender Breakdown per Race')

    # race = df["Event Name"]

    # gender = df["Gender"].value_counts()
  

    st.header('Participants sales per gender')
    genderTable = df.pivot_table(index='Gender',values=['Ticket Price', 'Total Price Paid Per Ticket'], aggfunc='sum')
    st.dataframe(genderTable)


    st.header('DUNNO YET')
    eventGenderTable = df.pivot_table(index='Event Name', values=['Gender'], aggfunc='count')
    st.dataframe(eventGenderTable)


    st.header('Gender Breakdown per Cycle')
    fig10, ax = plt.subplots()  # Create a figure containing a single axes.
    genderBreakPerCycles = df.groupby(['Event Name'])['Gender'].value_counts().plot(kind='pie')
    st.pyplot(fig10)


    # make data
    x = df['Event Year']
    y = df['Gender']

    # plot
    fig12, ax = plt.subplots()

    ax.plot(x, y)

    # ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
    #     ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()
    st.pyplot(fig12)


    st.header('Most Frequent Gender')
    gender1Table = df['Gender'].describe()
    st.dataframe(gender1Table)






    st.header('Participants Ticket sales per gender')
    genderValueTable = df.pivot_table(index='Gender', values=['Ticket Price', 'Total Price Paid Per Ticket'], aggfunc='sum')
    st.dataframe(genderValueTable)

    st.header('Participants Ticket sales per gender per Race')
    genderValuePerEventTable = df.pivot_table(index='Gender', columns='Event Name', values=['Ticket Price', 'Total Price Paid Per Ticket'], aggfunc='sum')
    st.dataframe(genderValuePerEventTable)

else:
    st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")