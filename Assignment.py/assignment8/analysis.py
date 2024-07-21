# analysis.py (shweta)

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

