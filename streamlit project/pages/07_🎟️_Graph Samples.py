import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl


uploaded_file = st.sidebar.file_uploader('Upload your file here')


# is file uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['df'] = df
    st.header('Data Statistics')
    st.write(df.describe())

    st.header ('Mean Price paid Per Ticket')
    meanTicketPrice = df['Total Price Paid Per Ticket'].mean()
    st.write(meanTicketPrice)


    # t = ['Total Price Paid Per Ticket']
    # pd.to_numeric(t, downcast='float')
    st.header ('Frequency of ticket price paid')
    # freqTicketPrice = df['Total Price Paid Per Ticket'].plot(kind='box', vert=False, figsize=(14,6))


    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.
    st.pyplot(fig)

    st.header ('Testing single axes')
    # fig1 = plt.figure()  # an empty figure with no Axes
    fig1, ax = plt.subplots()  # a figure with a single Axes
    st.pyplot(fig1)

    st.header ('Testing 2*2 grid of Axes')
    fig2, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
    st.pyplot(fig2)


    x = np.linspace(0, 2, 100)  # Sample data.

    st.header ('OO-style')
    # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
    fig3, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x, x, label='linear')  # Plot some data on the axes.
    ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
    ax.plot(x, x**3, label='cubic')  # ... and some more.
    ax.set_xlabel('x label')  # Add an x-label to the axes.
    ax.set_ylabel('y label')  # Add a y-label to the axes.
    ax.set_title("Simple Plot")  # Add a title to the axes.
    ax.legend();  # Add a legend.
    st.pyplot(fig3)

    st.header ('pyplot-style')
    # x = np.linspace(0, 2, 100)  # Sample data.
    plt.figure(figsize=(5, 2.7), layout='constrained')
    plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
    plt.plot(x, x**2, label='quadratic')  # etc.
    plt.plot(x, x**3, label='cubic')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title("Simple Plot")
    plt.legend()

    st.header ('Using a helper function')

    def my_plotter(ax, data1, data2, param_dict):
        """
        A helper function to make a graph.
        """
        out = ax.plot(data1, data2, **param_dict)
        return out


    data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
    fig5, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
    my_plotter(ax1, data1, data2, {'marker': 'x'})
    my_plotter(ax2, data3, data4, {'marker': 'o'})
    st.pyplot(fig5)


    st.header ('Styling Artists')

    fig6, ax = plt.subplots(figsize=(5, 2.7))
    x = np.arange(len(data1))
    ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
    l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
    l.set_linestyle(':')
    st.pyplot(fig6)


    st.header ('Colours')

    fig7, ax = plt.subplots(figsize=(5, 2.7))
    ax.scatter(data1, data2, s=50, facecolor='C0', edgecolor='k')
    st.pyplot(fig7)

    st.header ('Plotting Dates and Stings')
    fig8, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    dates = np.arange(np.datetime64('2021-11-15'), np.datetime64('2021-12-25'),
                    np.timedelta64(1, 'h'))
    data = np.cumsum(np.random.randn(len(dates)))
    ax.plot(dates, data)
    cdf = mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator())
    ax.xaxis.set_major_formatter(cdf)
    st.pyplot(fig8)
else:
    st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")