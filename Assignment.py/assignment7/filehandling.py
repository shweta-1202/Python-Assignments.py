# shweta fh file
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_cleaned_data(df):
    return pd.read_csv('country_wise_latest.csv')

def save_cleaned_data(df):
    df.to_csv('clean_covid_data.csv', index=False)