import streamlit as st
import matplotlib.pyplot as plt

df = st.session_state['df'] 

st.header('Plot of Data')

fig, ax = plt.subplots(1,1)
ax.scatter(x=df['Order Timestamp'], y=df['Total Price Paid Per Ticket'])
ax.set_xlabel('Order Timestamp')
ax.set_ylabel('Total Price Paid Per Ticket')

st.pyplot(fig)