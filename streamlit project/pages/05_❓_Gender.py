
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl

df = st.session_state['df'] 
st.header('Gender of participants')


fig9, ax = plt.subplots()  # Create a figure containing a single axes.
eventName = df["Event Name"]
gender = df["Gender"].value_counts()
colors = ["#1f77b4", "#ff7f0e"]
plt.pie(gender, labels=gender, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=120)
# plt.title("Gender breakdown\n"+"All Events")
st.pyplot(fig9)

st.header('Gender of participants Table')

genderTable = df.pivot_table(index='Gender', aggfunc='sum')
st.dataframe(genderTable)


genderValueTable = df.pivot_table(index='Gender', values=['Ticket Price', 'Total Price Paid Per Ticket'], aggfunc='sum')
st.dataframe(genderValueTable)



