# imports
import streamlit as st
# Exploratory packages
import pandas as pd
# Visualization packages
import matplotlib.pyplot as plt

DATA_URL="C:/Users/iamgu/Centennial/Semester 6/Data Warehouse/Project/dataset/Bicycle_Thefts.csv"

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
    st.title("COMP309 Project")
    # Get data from load_data method 
    data=load_data()
    st.subheader("Raw Data")
    # Writing data to streamlit
    if st.checkbox('View Data'):
        st.write(data)
    st.subheader("Map of bikes lost in toronto")
    if st.checkbox('View Map'):
        st.map(data)
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
