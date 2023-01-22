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


def interactive_plot(dataframe):
    x_axis_val = st.selectbox('Select X-Axis Value', options=df.columns)
    y_axis_val = st.selectbox('Select Y-Axis Value', options=df.columns)
    col = st.color_picker('Pick a Plot Colour')
    

    plot = px.scatter(dataframe, x=x_axis_val, y=y_axis_val)
    plot.update_traces(marker=dict(color=col))
    st.plotly_chart(plot)



st.title("Event Data Analysis Tool")
st.write("use current trends to visual further opportunities")
st.text("just input your data and this app will do the rest")
# st.markdown('This is a **bold**')
# st.markdown('## This is **level two header with bold**')

st.sidebar.title('Navigation')

uploaded_file = st.sidebar.file_uploader('Upload your file here')

options = st.sidebar.radio('Pages', options=['Home', 'Data Statistics', 'Data Header', 'Plot', 'Interactive Plot'])

if uploaded_file:
 
    df = pd.read_csv(uploaded_file)
    
   
if options == 'Data Statistics':
    stats(df)
elif options == 'Data Header':
    data_header(df)
elif options == 'Plot':
    plot(df)
elif options == 'Interactive Plot':
    interactive_plot(df)