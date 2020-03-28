# imports
import streamlit as st
from datetime import datetime
# Exploratory packages
import pandas as pd
# Visualization packages
import matplotlib.pyplot as plt


#  App Title
st.title('Toronto Bike Theft Analysis')
DATA_URL="dataset/Bicycle_Thefts.csv"

# Load the data into dataframe
@st.cache(allow_output_mutation=True )
def load_data():  
    data=pd.read_csv(DATA_URL, nrows=100)
    lowercase=lambda x: str(x).lower()
    data.rename(lowercase,axis='columns',inplace=True)
    data.rename(columns={'long':'lon'},inplace=True)
    return data

def main():
    # Assigning title and subheader
    # Get data from load_data method 
    data=load_data()
    data['daytime']=""
    addDaytimeColumn(data)

    # Writing data to streamlit
    if st.sidebar.checkbox('View Data'):
        st.write(data)
    
    if st.sidebar.checkbox('View Bike Info'):
        # filter unique bike status values for sidebar
        status=st.sidebar.selectbox('Select Bike Status',data.status.unique())
        # filter premise types values
        premise_type=st.sidebar.selectbox('Premise type', data.premise_type.unique())
        time=st.sidebar.selectbox('Select Time Interval',data.daytime.unique())
        # Adding daytime column 
        

        data_status=data[data.status==status]
        data_premise=data_status[data.premise_type==premise_type]
        data_map=data_premise[data.daytime==time]
        st.map(data_map)
        total_count=data_map.index_.count()
        st.text('Total count: %s' %  total_count)
    
    
    
def addDaytimeColumn(data):
    
    for index, occurrence_time in enumerate(data.occurrence_time):
        hour=datetime.strptime(occurrence_time,'%H:%M').time().hour
        if hour>=5 and hour<12:
            data['daytime'][index]='morning'
        elif hour>=12 and hour<18:
            data['daytime'][index]='afternoon'
        elif hour>=18 and hour<21:
            data['daytime'][index]='evening'
        else:
             data['daytime'][index]='night'  
    return data

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


