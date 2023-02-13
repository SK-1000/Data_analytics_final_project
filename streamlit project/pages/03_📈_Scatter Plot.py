import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

uploaded_file = st.sidebar.file_uploader('Upload your file here')


# is file uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['df'] = df

    st.header('Plot of Data')

    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Order Timestamp'], y=df['Total Price Paid Per Ticket'])
    ax.set_xlabel('Order Timestamp')
    ax.set_ylabel('Total Price Paid Per Ticket')

    st.pyplot(fig)
else:
    st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")