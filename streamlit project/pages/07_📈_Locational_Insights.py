
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
import folium
from streamlit_folium import st_folium


df = st.session_state['df']
PAGE_TITLE = 'Participant Counts and Profit Metrics'
PAGE_SUB_TITLE = 'Source: Inputted Data file'

    #filter participants by year,month, county and event name
# def display_participant_count_facts(df, year, month, county, event_name, metric_title, number_format='{:,}'):
#     df = df[(df['Booking Year'] == year) & (df['Booking Month'] == month) & (df['Event Name'] == event_name)]
#     if county:
#         df = df[df['County'] == county]

#     total = len(df.index) #counts number of rows
#     st.metric(metric_title, number_format.format(round(total)))

@st.cache_data
def display_participant_facts(df, year, month, county, metric_title, number_format='€{:,}', is_median =False, need_count=False): #added a variable for euro
    df = df[(df['Booking Year'] == year) & (df['Booking Month'] == month)]
    if county:
        df = df[df['County'] == county]
    if is_median:
        total = df[field_name].median() #gives median profit
    else:
        total = df[field_name].sum() #sums profit
    if need_count:
        total = len(df.index) #counts number of rows
    st.metric(metric_title, number_format.format(round(total)))


# @st.cache_data
# def display_participant_facts(df, year, month, county, event_name, metric_title, number_format='€{:,}', is_median =False, need_count=False): #added a variable for euro
#     df = df[(df['Booking Year'] == year) & (df['Booking Month'] == month) & (df['Event Name'] == event_name)]
#     if county:
#         df = df[df['County'] == county]
#     if is_median:
#         total = df[field_name].median() #gives median profit
#     else:
#         total = df[field_name].sum() #sums profit
#     if need_count:
#         total = len(df.index) #counts number of rows
#     st.metric(metric_title, number_format.format(round(total)))
# TEST ADDING A CACHE HERE

def display_map(df, year, month):

    # st.header('Counties by Participant Count')
    # df = df.assign(count=1).pivot_table(index=('County', 'Booking Year', 'Booking Month'), values='count', aggfunc='sum', fill_value=0)
    # st.dataframe(df)

    df = df[(df['Booking Year'] == year) & (df['Booking Month'] == month)]
  
    map = folium.Map(location=[53.393075, -7.742133], zoom_start=7, scrollWheelZoom=False, tiles='cartoDB positron') # calling the map class from the folium library. Coordinates are centre of Ireland and disabled scroll wheel
    
   
    choropleth = folium.Choropleth(
        geo_data='data/Counties.geojson.txt',
        data=df,
        columns=('County', 'Participant Count'),
        key_on='feature.properties.COUNTY',
        line_opacity=0.7,
        line_color='blue',
        highlight=True
    )
    choropleth.geojson.add_to(map)
   
    df = df.set_index('County')
    county = 'DUBLIN'
    
    #This is currently filtered by booking year and booking month.


    for feature in choropleth.geojson.data['features']:
        county = feature['properties']['COUNTY']
        feature['properties']['PARTICIPANTS'] = '  ' + str(df.loc[county, 'Participant Count'].sum() if county in list(df.index) else 'N/A') 
        #found the sum of each county and put it to the geoJason as a property called participant.I took the county name from data fram and converted it as a string.
        # There was an issue whereby some counties were not available in my data for this filtered period so I added a condition taht 
        #if the fieldname is available in the geoJason and also available in my dataframe, it will display otherwise it wont display.
        feature['properties']['PROFIT'] = '  ' + str(df.loc[county, 'Profit Per Ticket'].sum() if county in list(df.index) else 'N/A')
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['COUNTY', 'PROVINCE', 'PARTICIPANTS','PROFIT'])
    )
    st_map = st_folium(map, width=700, height=450) #return the map object into the streamlit folium library to display map
    county = ''
    if st_map['last_active_drawing']:
        county = st_map['last_active_drawing']['properties']['COUNTY']
    return county



def main():
    st.set_page_config(PAGE_TITLE)
    st.title(PAGE_TITLE)
    st.caption(PAGE_SUB_TITLE)



#removes the default burger menu
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)



# is file uploaded
if df is not None:
#filterable variables
    year = 2021
    month = 'January'
    county = ''
    # event_name = 'Cycle Kerry'
    field_name = 'Profit Per Ticket'
    metric_title = f'No. of {county} Participants' #Included the event name variable

    #display filters and map
    year_list = list(df['Booking Year'].unique())
    year_list.sort(reverse=True)
    
    year = st.sidebar.selectbox('Booking Year', year_list)

    month_list = list(df['Booking Month'].unique())
    month_list.sort()
    
    month = st.sidebar.selectbox('Booking Month', month_list)


    st.header(f'{county} {year} {month}')

    county = display_map(df, year, month)
    # display_map(df, year, month)

    #display metrics
    st.subheader(f'{county} Metrics')
    #call functions
    col1, col2, col3 = st.columns(3)
    with col1:
        display_participant_facts(df, year, month, county, f'No. of {county} Participants',number_format='{:,}',is_median=True, need_count=True)
    with col2:
        display_participant_facts(df, year, month, county, 'Total EUR Profit')
    with col3:
        display_participant_facts(df, year, month, county,  'Median EUR Profit',is_median=True)
   
    #     #display metrics
    # st.subheader(f'{event_name} Metrics')
    # #call functions
    # col1, col2, col3 = st.columns(3)
    # with col1:
    #     display_participant_facts(df, year, month, county, event_name, f'No. of {event_name} Participants',number_format='{:,}',is_median=True, need_count=True)
    # with col2:
    #     display_participant_facts(df, year, month, county, event_name, 'Total EUR Profit')
    # with col3:
    #     display_participant_facts(df, year, month, county, event_name, 'Median EUR Profit',is_median=True)

    #exploring data

    # st.write(df.shape)
    # st.write(df.head())
    # st.write(df.columns)
   
    

    st.header('Participants Age Category per Annum')
    AgeCatCountPerYearTable = df.assign(count=1).pivot_table(index='Event Year', columns = 'Age Category', values='count', aggfunc='sum', fill_value=0)
    st.dataframe(AgeCatCountPerYearTable)
    #test
    st.header('Counties by Participant Count')
    AgeCatCountPerYearTable = df.assign(count=1).pivot_table(index='County', values='count', aggfunc='sum', fill_value=0)
    st.dataframe(AgeCatCountPerYearTable)

    st.header('Counties by Participant Count per Age Category')
    AgeCatCountPerYearTable = df.assign(count=1).pivot_table(index='County', columns = 'Age Category', values='count', aggfunc='sum', fill_value=0)
    st.dataframe(AgeCatCountPerYearTable)


    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(df)
else:
    # st.write("REMEMBER TO UPLOAD A FILE IN ORDER TO VIEW DATA")
    st.warning('Please Upload Your Data File for Analysis')



#call main function
if __name__ == "__main__":
    main()