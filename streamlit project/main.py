import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px



def stats(dataframe):
    st.header('Data Statistics')
    st.write(dataframe.describe())

def data_header(dataframe):
    st.header ('Data Header')
    st.write(dataframe.head())

def plot(dataframe):
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Order Timestamp'], y=df['Total Price Paid Per Ticket'])
    ax.set_xlabel('Order Timestamp')
    ax.set_ylabel('Total Price Paid Per Ticket')

    st.pyplot(fig)


st.title("Event Data Analysis Tool")
st.write("use current trends to visual further opportunities")
st.text("just input your data and this app will do the rest")
# st.markdown('This is a **bold**')
# st.markdown('## This is **level two header with bold**')

st.sidebar.title('Navigation')

uploaded_file = st.sidebar.file_uploader('Upload your file here')

options = st.sidebar.radio('Pages', options=['Home', 'Data Statistics', 'Data Header', 'Plot'])

if uploaded_file:
 
    df = pd.read_csv(uploaded_file)
    
   
if options == 'Data Statistics':
    stats(df)
elif options == 'Data Header':
    data_header(df)
elif options == 'Plot':
    plot(df)
