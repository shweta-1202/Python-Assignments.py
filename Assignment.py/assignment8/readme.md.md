# COVID-19 Data Visualization and Dashboard

<------------------------------Data_Cleaning------------------------------------------------>

--Load Data: Loads the CSV file (country_wise_latest.csv) into a pandas DataFrame. Handles errors like empty file, parsing errors, or file not found.
--Clean Data: Cleans the loaded data by:
--Displaying the original DataFrame.
--Handling missing values and displaying the count per column.
--Handling duplicate rows and displaying the count.
--Dropping duplicates and filling missing values with 0.
--Converting the 'Date' column to datetime if it exists.
--Displaying the cleaned DataFrame.
<-----------------------------------File_handling-------------------------------------------------->

--Load and Clean Data:The app will display the original data, perform basic data cleaning tasks such as handling missing values and duplicates, and show the cleaned data.
--Save Cleaned Data:After cleaning, the cleaned data can be saved to clean_covid_data.csv using the provided functionality in data_cleaning.py.

<---------------------------------------Exception---------------------------------------->
--When an error occurs during data cleaning, you can raise a DataCleaningError to provide a clear indication of what went wrong. This helps in debugging and understanding specific issues encountered during data processing.

<-----------------------------------------Visualization------------------------------------------>
--Generates plots for total Confirmed, Deaths, and Recovered cases of each country.
Also generates a plot for total cases in top 10 countries.
--load_data(df): Loads the cleaned COVID-19 data from clean_covid_data.csv into a pandas DataFrame.
--plot_total_cases(df):Generates bar charts showing the total confirmed, deaths, and recovered cases for each country.
--plot_top_countries(df): Displays a stacked bar chart showing the top 10 countries with the highest number of confirmed COVID-19 cases.
--Entry point of the script. Loads the data and calls the plotting functions.

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load the cleaned dataset
def load_data():
    try:
        df = pd.read_csv('clean_covid_data.csv')
    except FileNotFoundError:
        st.error("File 'clean_covid_data.csv' not found.")
        st.stop()
    return df

# Function to run the dashboard
def run_dashboard():
    st.title('COVID-19 Data Visualization Dashboard')
    
    # Load the dataset
    df = load_data()
    
    # User inputs
    countries = st.multiselect('Select Country/Region', df['Country/Region'].unique())
    case_type = st.selectbox('Select Case Type', ['Confirmed', 'Deaths', 'Recovered'])
    filtered_data = df[df['Country/Region'].isin(countries)]
    
    # Function to plot bar chart
    def plot_bar_chart(data, case_type):
        plt.figure(figsize=(10, 6))
        data.groupby('Country/Region').sum()[case_type].plot(kind='bar', color='yellow')
        plt.xlabel('Country/Region')
        plt.ylabel(f'Number of {case_type} Cases')
        plt.title(f'Total {case_type} Cases by Country/Region')
        plt.xticks(rotation=45)
        st.pyplot(plt)
    
    # Display the bar chart based on user selections
    if st.button('Generate Bar Chart'):
        if filtered_data.empty:
            st.warning("No data available for the selected filters.")
        else:
            plot_bar_chart(filtered_data, case_type)

# Main block to run the Streamlit app
if __name__ == '__main__':
    run_dashboard()


<---------------------------------Dashboard---------------------------------------------------------->
    Creates a Streamlit dashboard for user interactive data visualization.
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load the cleaned dataset
def load_data():
    try:
        df = pd.read_csv('clean_covid_data.csv')
    except FileNotFoundError:
        st.error("File 'clean_covid_data.csv' not found.")
        st.stop()
    return df

# Function to run the dashboard
def run_dashboard():
    st.title('COVID-19 Data Visualization Dashboard')
    
    # Load the dataset
    df = load_data()
    
    # User inputs
    countries = st.multiselect('Select Country/Region', df['Country/Region'].unique())
    case_type = st.selectbox('Select Case Type', ['Confirmed', 'Deaths', 'Recovered'])
    filtered_data = df[df['Country/Region'].isin(countries)]
    
    # Function to plot bar chart
    def plot_bar_chart(data, case_type):
        plt.figure(figsize=(10, 6))
        data.groupby('Country/Region').sum()[case_type].plot(kind='bar', color='yellow')
        plt.xlabel('Country/Region')
        plt.ylabel(f'Number of {case_type} Cases')
        plt.title(f'Total {case_type} Cases by Country/Region')
        plt.xticks(rotation=45)
        st.pyplot(plt)
    
    # Display the bar chart based on user selections
    if st.button('Generate Bar Chart'):
        if filtered_data.empty:
            st.warning("No data available for the selected filters.")
        else:
            plot_bar_chart(filtered_data, case_type)

# Main block to run the Streamlit app
if __name__ == '__main__':
    run_dashboard()

<-----------------------------Analysis----------------------------------------------->
Organize/Arrange data cleaning, visualization, and dashboard creation.
import visualization
import dashboard
import file_handling
import exceptions
import data_cleaning

def main():
    # Read the dataset
    df = file_handling.read_csv('clean_covid_data.csv')

    try:
        # Clean the data
        df = data_cleaning.clean_data(df)
        
        # Write cleaned data to CSV
        file_handling.write_csv(df, 'clean_covid_data.csv')
        
    except exceptions.DataCleaningError as e:
        print(f"Data cleaning error: {e}")
        return

    # Plot visualizations
    visualization.plot_total_cases(df)
    visualization.plot_top_countries(df)


    # Create dashboard (assuming dashboard.py has a function named create_dashboard)
    dashboard.create_dashboard(df)

main()
