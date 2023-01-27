import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px
# import pickle
# from pathlib import Path
import streamlit_authenticator as stauth
import database as db



# headers, titles and text
st.title("Event Data Analysis Tool")
st.write("use current trends to visual further opportunities")
st.text("just input your data and this app will do the rest")



# functions for pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Explore using the navigation menu on the left')
    else:
        st.header('To start please upload a file')

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


#sidebar code

st.sidebar.title('Navigation')


uploaded_file = st.sidebar.file_uploader('Upload your file here')
# options = st.sidebar.radio('Pages', options=['Home', 'Data Statistics', 'Data Header', 'Plot', 'Interactive Plot'])


# is file uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['df'] = df


# # Navigation
# if options == 'Data Statistics':
#     stats(df)
# elif options == 'Data Header':
#     data_header(df)
# elif options == 'Plot':
#     plot(df)
# elif options == 'Interactive Plot':
#     interactive_plot(df)