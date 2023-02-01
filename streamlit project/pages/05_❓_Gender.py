
import streamlit as st
import plotly.express as px
import plotly

# df = st.session_state['df'] 
st.header('Gender of participants')


values = df['Results']
names = df['Category']


fig = px.pie(df, values = values, names = names, title = 'Gender Results')





fig.update_traces(
            textposition = 'inside',
            textinfo='percent+label'
            )

fig.update_layout(
            title_font_size = 42
                )


plotly.offline.plot(fig,filename='Piechart.html')