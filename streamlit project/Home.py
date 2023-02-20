import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px
import streamlit_authenticator as stauth
import database as db

from PIL import Image
# Loading Image using PIL
im = Image.open('./content/dudeonbike.jfif')
# This widens the space on the page where data is displayed and adds and image and title to the tab
st.set_page_config(layout="wide", page_title="Event Data App", page_icon = im)

#removes the default burger menu
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


# headers, titles and text
st.title("Event Data Analysis Tool")
st.write("Use current trends to visual further opportunities")
st.write("Simply input your data and this app will do the rest")
st.image('./content/cycle.png',width=500)


# functions for pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Explore using the navigation menu on the left')
    else:
        st.header('To start please upload a file')

# def stats(dataframe):
#     st.header('Data Statistics')
#     st.write(dataframe.describe())

# def data_header(dataframe):
#     st.header ('Data Header')
#     st.write(dataframe.head())

# def plot(dataframe):
#     fig, ax = plt.subplots(1,1)
#     ax.scatter(x=df['Order Timestamp'], y=df['Total Price Paid Per Ticket'])
#     ax.set_xlabel('Order Timestamp')
#     ax.set_ylabel('Total Price Paid Per Ticket')

#     st.pyplot(fig)


# def interactive_plot(dataframe):
#     x_axis_val = st.selectbox('Select X-Axis Value', options=df.columns)
#     y_axis_val = st.selectbox('Select Y-Axis Value', options=df.columns)
#     col = st.color_picker('Pick a Plot Colour')


#     plot = px.scatter(dataframe, x=x_axis_val, y=y_axis_val)
#     plot.update_traces(marker=dict(color=col))
#     st.plotly_chart(plot)



#sidebar code

st.sidebar.title('Navigation')


uploaded_file = st.sidebar.file_uploader('Upload your file here')
# options = st.sidebar.radio('Pages', options=['Home', 'Data Statistics', 'Data Header', 'Plot', 'Interactive Plot'])


# is file uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['df'] = df
else:
    st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")
    


# # Navigation
# if options == 'Data Statistics':
#     stats(df)
# elif options == 'Data Header':
#     data_header(df)
# elif options == 'Plot':
#     plot(df)
# elif options == 'Interactive Plot':
#     interactive_plot(df)