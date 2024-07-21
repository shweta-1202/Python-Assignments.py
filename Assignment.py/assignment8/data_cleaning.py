# data_cleaning.py(sp)

import pandas as pd
import streamlit as st
from exceptions import DataCleaningError  

def load_data(df):
    try:
        df = pd.read_csv('country_wise_latest.csv')  # Load the CSV file into a DataFrame
        return df
    except pd.errors.EmptyDataError:
        raise DataCleaningError("No data in the file.")  # Raise custom error if the file is empty
    except pd.errors.ParserError:
        raise DataCleaningError("Error parsing the file.")  # Raise custom error if there is a parsing error
    except FileNotFoundError:
        raise DataCleaningError(f"File {'country_wise_latest.csv'} not found.")  # Raise custom error if the file is not found

def clean_data(df):
    st.write("Original DataFrame:")
    st.write(df)  
    
    st.subheader("Data Cleaning Process:")
    
    # Handle missing values
    st.write("Missing values per column:")
    st.write(df.isna().sum())  # Display the count of missing values per column
    
    # Handle duplicate rows
    st.write("Number of duplicate rows:")
    st.write(df.duplicated().sum())  # Display the count of duplicate rows
    
    # Drop duplicates and fill missing values
    df = df.drop_duplicates()  # Drop duplicate rows
    df = df.fillna(0)  # Fill missing values with 0
    
    # Convert 'Date' column to datetime if it exists
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    st.write("Cleaned DataFrame:")
    st.write(df)  
    
    return df
