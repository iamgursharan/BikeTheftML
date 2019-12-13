# imports
import streamlit as st
# Exploratory packages
import pandas as pd
# Visualization packages
import matplotlib.pyplot as plt

DATA_URL="C:/Users/300931676/DataAnalysisUsingStreamlit/dataset/Bicycle_Thefts.csv"

# @st.cache(suppress_st_warning=True)

# Load the data into dataframe
def load_data():  
    data=pd.read_csv(DATA_URL)
    lowercase=lambda x: str(x).lower()
    data.rename(lowercase,axis='columns',inplace=True)
    data.rename(columns={'long':'lon'},inplace=True)
    return data

def main():
    # Assigning title and subheader
    # Get data from load_data method 
    data=load_data()
    st.subheader("Raw Data")
    # Writing data to streamlit
    if st.checkbox('View Data'):
        st.write(data)
    st.subheader("Map of lost bikes")
    if st.checkbox('View Map'):
        status=st.selectbox('Select status',data.status.unique())
        hour=st.selectbox('Select hour',data.occurrence_time.unique())
        data_status=data[data.status==status]
        data_map=data_status[data.occurrence_time==hour]
        st.map(data_map)
        total_count=data_map.status.count()
        st.text('Total count: %s' %  total_count)
    if st.checkbox('Visualize'):
        visualize_data(data)
    

    


def visualize_data(data):
    if st.checkbox('Visualize bike make'):
        stolen_bike_make=data.loc[data.status=='STOLEN']['bike_make']
        st.text('Total count of stolen bikes by make: %s'% stolen_bike_make.count())
        st.bar_chart(stolen_bike_make.value_counts())

    if st.checkbox('Visualize bike type'):
        stolen_bike_type=data.loc[data.status=='STOLEN']['bike_type']
        st.text('Total count of stolen bikes by type: %s'% stolen_bike_type.count())
        st.bar_chart(stolen_bike_type.value_counts()) 
        

    
if __name__== '__main__':
    main()
