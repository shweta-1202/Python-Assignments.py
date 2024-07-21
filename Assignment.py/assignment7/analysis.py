# shweta ana_file

import pandas as pd
import streamlit as st
from data_cleaning import clean_data, load_data  # Import custom data cleaning functions
from filehandling import load_cleaned_data, save_cleaned_data  # Import file handling functions
from exceptions import DataCleaningError  # Import user exception

file_name = 'country_wise_latest.csv'  # Original data file name
cleaned_file_name = 'clean_covid_data.csv'  # Cleaned data file name

try:
    # Load original data
    df = load_data('country_wise_latest.csv')  
    st.write("Original Data ")  # Display header for original data
    st.write(df)  # Display first few rows of the original data
    
    # Clean data
    df = clean_data(df)  
    
    # Save cleaned data
    save_cleaned_data(df)  
    
    st.write('Cleaned Data ')  # Display header for cleaned data
    
    # Load cleaned data
    df = load_cleaned_data('country_wise_latest.csv')  
    st.write(df)  # Display first few rows of the cleaned data
    
    # Calculate totals
    total_cases = df['Confirmed'].sum()  # Calculate total confirmed cases
    total_deaths = df['Deaths'].sum()  # Calculate total deaths
    total_recovered = df['Recovered'].sum()  # Calculate total recoveries

    st.subheader("All Over")  # Subheader for totals section
    st.write("Total Cases:", total_cases)  # Display total confirmed cases
    st.write("Total Deaths:", total_deaths)  # Display total deaths
    st.write("Total Recovered:", total_recovered)  # Display total recoveries

    # Button to show top/bottom countries/states by cases
    show_top_bottom = st.button("Show top/bottom 10 countries/states by cases")

    if show_top_bottom:
        # Group by country/region and sum confirmed cases, then sort
        country_cases = df.groupby("Country/Region")["Confirmed"].sum().reset_index()
        country_cases = country_cases.sort_values("Confirmed", ascending=False)

        st.write("Top 10 countries/states by cases:")
        top_10 = country_cases.head(10)
        st.write(top_10)  # Display top 10 countries/states by cases

        st.write("Bottom 10 countries/states by cases:")
        bottom_10 = country_cases.tail(10)
        st.write(bottom_10)  # Display bottom 10 countries/states by cases

        # Visualization using Streamlit's st.bar_chart
        st.subheader("Top 10 Countries/Regions by Confirmed Cases")
        st.bar_chart(top_10.set_index("Country/Region"), color='#FFC0CB')  # Bar chart for top 10 countries

        st.subheader("Bottom 10 Countries/Regions by Confirmed Cases")
        st.bar_chart(bottom_10.set_index("Country/Region"), color='#90EE90')  # Bar chart for bottom 10 countries

except DataCleaningError as e:
    st.error(f"Data Cleaning Error: {e.message}")  # Display error message for data cleaning errors
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")  # Display error message for unexpected errors

