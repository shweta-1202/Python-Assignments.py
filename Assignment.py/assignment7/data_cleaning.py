# shweta dc_file


import pandas as pd
import streamlit as st
from exceptions import DataCleaningError

def load_data(df):
    try:
        df = pd.read_csv('country_wise_latest.csv')
        return df
    except pd.errors.EmptyDataError:
        raise DataCleaningError("No data in the file.")
    except pd.errors.ParserError:
        raise DataCleaningError("Error parsing the file.")
    except FileNotFoundError:
        raise DataCleaningError(f"File {'country_wise_latest.csv'}not found.")

def clean_data(df):
    st.write("Original DataFrame:")
    st.write(df)  # Display the first few rows of the original data
    
    st.subheader("Data Cleaning Process:")
    
    # Handle missing values
    st.write("Missing values per column:")
    st.write(df.isna().sum())
    
    # Handle duplicate rows
    st.write("Number of duplicate rows:")
    st.write(df.duplicated().sum())
    
    # Drop duplicates and fill missing values
    df = df.drop_duplicates()
    df = df.fillna(0)

    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    

    st.write("Cleaned DataFrame:")
    st.write(df)  # Display the first few rows of the cleaned data
    
    return df



