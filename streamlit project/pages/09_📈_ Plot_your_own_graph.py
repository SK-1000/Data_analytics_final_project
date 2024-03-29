# Author Sheila Kirwan
# This page contains plotly express scatter plot however for this plot, the user can select the x and the y axix
# from the list of columns in the data inputted.

import streamlit as st
import plotly_express as px
import pandas as pd
import sys

df = st.session_state['df']
pageSubTitle = 'Source: Inputted Data file'
st.markdown("<h1 style='text-align: center; color: white;'>Plot Your Own Graph</h1>", unsafe_allow_html=True)
st.title('Plot')

#removes the default burger menu
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


#double check to ensure my project is inside virtual environment
def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

if is_venv():
    print('inside virtualenv or venv')
else:
    print('outside virtualenv or venv')


# is file uploaded
if df is not None:
  
    col1, col2 = st.columns(2)

    x_axis_val = col1.selectbox('Select X-Axis Value', options=df.columns)
    y_axis_val = col2.selectbox('Select Y-Axis Value', options=df.columns)
    col = st.color_picker('Pick a Plot Colour')
        
    plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
    plot.update_traces(marker=dict(color=col))
    st.plotly_chart(plot, use_container_width=True)
else:
    # st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")
    st.warning('Please Upload Your Data File for Analysis')