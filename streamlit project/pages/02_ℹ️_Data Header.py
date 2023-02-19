import streamlit as st
import pandas as pd

# df = st.session_state['df'] 


uploaded_file = st.sidebar.file_uploader('Upload your file here')


# is file uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['df'] = df
    st.header ('Data Header')
    st.write(df.head())
    st.header ('Data Shape')
    st.write(df.shape)
else:
    st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")