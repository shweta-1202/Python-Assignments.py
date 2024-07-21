# file_handling.py(shweta)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load cleaned data from 'country_wise_latest.csv'
def load_cleaned_data(df):
    return pd.read_csv('country_wise_latest.csv')

# Function to save cleaned data to 'clean_covid_data.csv'
def save_cleaned_data(df):
    df.to_csv('clean_covid_data.csv', index=False)  # Save DataFrame to CSV without including index
