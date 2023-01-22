import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Event Data Analysis Tool")
st.write("use current trends to visual further opportunities")
st.text("just input your data and this app will do the rest")
st.markdown('This is a **bold**')
st.markdown('## This is **level two header with bold**')

uploaded_file = st.file_uploader('Upload your file here')

if uploaded_file:
    st.header('Data Statistics')
    df = pd.read_csv(uploaded_file)
    st.write(df.describe())
    st.header ('Data Header')
    st.write(df.head())

    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Order Timestamp'], y=df['Total Price Paid Per Ticket'])
    ax.set_xlabel('Order Timestamp')
    ax.set_ylabel('Total Price Paid Per Ticket')

    st.pyplot(fig)