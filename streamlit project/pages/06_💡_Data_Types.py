import streamlit as st

df = st.session_state['df'] 
st.header ('Data Types')
info = df.info()
st.write(info)


