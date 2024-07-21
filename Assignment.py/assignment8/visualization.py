#visualization.py  (shweta)
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Function to load data from CSV file
def load_data(df):
    return pd.read_csv('clean_covid_data.csv')

# Function to plot total cases by country for all countries
def plot_total_cases(df):
    # Group data by 'Country/Region' and calculate total cases
    df_country = df.groupby('Country/Region').sum()
    countries = df_country.index.tolist()  # Get list of countries
    
    st.title('Total Confirmed, Deaths, and Recovered Cases by Country/Region')
    
    for country in countries:
        # Prepare data for the current country
        df_total = df_country.loc[country, ['Confirmed', 'Deaths', 'Recovered']].to_frame().reset_index()
        df_total.columns = ['CaseType', 'Count']  # Rename columns
        
        # Plotting
        fig, ax = plt.subplots(figsize=(10, 6))  # Create figure and axis
        ax.bar(df_total['CaseType'], df_total['Count'], color=['blue', 'yellow', 'green'])  # Bar chart
        ax.set_xlabel('Case Type')  # X-axis label
        ax.set_ylabel('Count')  # Y-axis label
        ax.set_title(f'Total Confirmed, Deaths, and Recovered Cases in {country}')  # Plot title
        st.pyplot(fig)  # Display plot in Streamlit app
        plt.close()  # Close plot to avoid overlapping in Streamlit

# Function to plot top 10 countries with highest cases
def plot_top_countries(df):
    # Group data by 'Country/Region', sum, and sort by 'Confirmed' descending
    df_country = df.groupby('Country/Region').sum().sort_values(by='Confirmed', ascending=False).head(10)
    df_top_countries = df_country[['Confirmed', 'Deaths', 'Recovered']]  # Select relevant columns
    
    st.title('Top 10 Countries with Highest Number of Cases')
    fig, ax = plt.subplots(figsize=(15, 8))  # Create figure and axis
    df_top_countries.plot(kind='bar', ax=ax)  # Bar chart
    ax.set_xlabel('Country/Region')  # X-axis label
    ax.set_ylabel('Count')  # Y-axis label
    ax.set_title('Top 10 Countries with Highest Number of Cases')  # Plot title
    ax.legend(['Confirmed', 'Deaths', 'Recovered'])  # Legend for plot
    st.pyplot(fig)  # Display plot in Streamlit app
    plt.close()  # Close plot to avoid overlapping in Streamlit

def main():
    # Load data
    df = load_data('clean_covid_data.csv')
    
    # Display total cases by country
    plot_total_cases(df)
    
    # Display top 10 countries with highest cases
    plot_top_countries(df)

if __name__ == "__main__":
    main()

