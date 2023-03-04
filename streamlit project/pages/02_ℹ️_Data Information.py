# Author Sheila Kirwan
# This streamlit page displays information on the inputted data file.
import streamlit as st
import pandas as pd

pageSubTitle = 'Source: Inputted Data file'
st.markdown("<h1 style='text-align: center; color: white;'>Data Information</h1>", unsafe_allow_html=True)




# df = st.session_state['df'] 




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


    df2 = df.head()

    @st.cache
    def convert_df(df2):
        # NB The Cache Memorises the function so that resources are not wasted by downloading on every run
        return df2.to_csv().encode('utf-8')

    csv = convert_df(df2)
    
    st.header ('Subset of the first rows of date from the inputted file')
    st.write(df2)

    st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='df.csv',
    mime='text/csv',
)
   

    #creating new dataframe that drops any column with N/A
    df4=df.drop(["Public health measures for COVID-19", "I have read  and agree to abide by the above Public health measures for COVID-19",
         " understand", " and agree to abide by the above Public health measures for COVID-19", "Privacy Policy", "Refund and Transfer Policy", 
         "Cycling Ireland Licence Number", "Club", "Rider Category", 'UCI ID', 'Date of Purchase', 'Active Order Number', 'Active CI Member', 'Active CI Number',
         'Active County', 'Active Mobile', 'Comment', 'Fundraiser Status'], axis = 1)
    st.header('Data Statistics')
    
    st.dataframe(df4.describe())


    st.header ('Data Shape - count of rows and columns')
    # adding metrics for the number of columns and rows in the file.
    metric_title = 'Number of Columns in the File'
    metric_title1 = 'Number of Rows in the File'

    col1, col2 = st.columns(2)
    with col1:
        rows = len(df) # counts the number of rows
        st.metric(metric_title, format(round(rows)))
    with col2:
        columns = df.shape[1] # counts the number of columns
        st.metric(metric_title1, format(round(columns)))
 

    def load_data():
        return pd.DataFrame(
            {
                "Rows": [5500],
                "Columns": [76],
            }
        )

    # This is a Boolean which will change the width of the dataframe, which is stored as a session state variable
    st.checkbox("Use container width", value=False, key="use_container_width")

    df = load_data()

    # Display the dataframe and allow the user to stretch the dataframe
    # across the full width of the container, based on the checkbox value
    st.dataframe(df, use_container_width=st.session_state.use_container_width)



    
else:
    st.markdown("<h5 style='text-align: center; color: White;'>Please Upload Your Data File for Analysis</h5>", unsafe_allow_html=True)