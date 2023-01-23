import streamlit as st
import plotly_express as px

df = st.session_state['df'] 

col1, col2 = st.columns(2)

x_axis_val = col1.selectbox('Select X-Axis Value', options=df.columns)
y_axis_val = col2.selectbox('Select Y-Axis Value', options=df.columns)
col = st.color_picker('Pick a Plot Colour')
    
plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
plot.update_traces(marker=dict(color=col))
st.plotly_chart(plot, use_container_width=True)