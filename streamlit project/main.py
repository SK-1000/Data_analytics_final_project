import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px
import pickle
from pathlib import Path
import streamlit_authenticator as stauth


# headers, titles and text
st.title("Event Data Analysis Tool")
st.write("use current trends to visual further opportunities")
st.text("just input your data and this app will do the rest")
# st.markdown('This is a **bold**')
# st.markdown('## This is **level two header with bold**')


# user authentication
names = ["Sheila Kirwan", "Oliver Kirwan"]
usernames = ["skirwan", "okirwan"]
passwords = ["hello", "hey"]

hashed_passwords = stauth.Hasher(passwords).generate()


credentials = {
        "usernames":{
            "jsmith92":{
                "name":"john smith",
                "password":"$2b$12$TSuKwWML0EpbohBQgHx4p8E5q"
                },
            "tturner":{
                "name":"timmy turner",
                "password":"$2b$12$asdaUduuibuEIyBUBHASD896a"
                }            
            }
        }

#load hashed passwords
file_path = Path(__file__).parent / "hashed_pkl.pkl"
with file_path.open("rb") as file:
    hashed_passwords  = pickle.load(file)

authenticator = stauth.Authenticate(credentials, "participation dashboard", "bcdefg", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Either your username or password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
   

# # functions for pages
# def home(uploaded_file):
#     if uploaded_file:
#         st.header('Explore using the navigation menu on the left')
#     else:
#         st.header('To start please upload a file')
    
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

# st.sidebar.title('Navigation')
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"welcome {name}")
    uploaded_file = st.sidebar.file_uploader('Upload your file here')
# options = st.sidebar.radio('Pages', options=['Home', 'Data Statistics', 'Data Header', 'Plot', 'Interactive Plot'])


# is file uploaded
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state['df'] = df
    

# Navigation
# if options == 'Data Statistics':
#     stats(df)
# elif options == 'Data Header':
#     data_header(df)
# elif options == 'Plot':
#     plot(df)
# elif options == 'Interactive Plot':
#     interactive_plot(df)