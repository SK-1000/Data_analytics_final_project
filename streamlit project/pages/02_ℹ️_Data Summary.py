import streamlit as st
import pandas as pd


uploaded_file = st.sidebar.file_uploader('Upload your file here')


# is file uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['df'] = df
    st.header('Data Statistics')
    st.write(df.describe())
else:
    st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")