import streamlit as st
import pandas as pd

df = st.session_state['df']



pageSubTitle = 'Source: Inputted Data file'
st.markdown("<h1 style='text-align: center; color: white;'>Data Type Information</h1>", unsafe_allow_html=True)
st.title('Data Types')
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
    # st.markdown("<h1 style='text-align: center; color: white;'>Data Type Information</h1>", unsafe_allow_html=True)
    st.caption(pageSubTitle)


    @st.cache_data
    def convert_df(df3):
        # NB The Cache Memorises the function so that resources and wasted on every run
        return df3.to_csv().encode('utf-8')
    

    col1 = 'Column Names'
    col2 = 'Column Data Types'
    df3 = pd.DataFrame(df.dtypes)
    st.table(df3)

    csv = convert_df(df3)

    st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='FileDataTypes.csv',
    mime='text/csv',
)
   
else:
    # st.markdown("<h5 style='text-align: center; color: White;'>Please Upload Your Data File for Analysis</h5>", unsafe_allow_html=True)
    st.warning('Please Upload Your Data File for Analysis')
