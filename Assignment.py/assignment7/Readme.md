<!-- shweta readme.md -->


<!-- **Documentation (README.md):**
- Explain what the dataset is about and why it's relevant.
- Provide clear instructions on how to run the code.
- Document the steps you took for data cleaning, file handling, and exception handling.
- Include examples of code snippets that demonstrate how exceptions are raised and handled. -->

Explain what the dataset is about
---The dataset describes the Covid-19 cases in various countries/states. 
---It gives us the number of confirmed cases, recoverd cases, active cases, and many more details.

Steps to run the program 
1. Run the data_cleaning.py file.
   -The data cleaning process involves loading the dataset, handling missing values, removing duplicates.

2. Run the Exception.py file.
   -Custom exceptions are defined in 'exception.py 'and handled throughout the project to manage errors effectively.

3. Run the file_handling.py file.
    -File handling functions are used for saving cleaned data and loading data from files.

4. Run the analysis.py file.
    - Open a terminal or command prompt.
    - Navigate to the project directory.
    - Execute the following command:
        streamlit run analysis.py
       

Document the steps you took for data cleaning, file handling, and exception handling.
1. Data Cleaning
-> A data_cleaning python file with .py extension is created.
->In this file a function is created named load_data.
->Also the clean_data function is created.
-> In clean_data function there are various methods used to clean the data.

-> Methods such as:
   1.dropna(inplace=True) is used to drop the columns which consist null values.
   2.duplicated().sum() is used to check the duplicate/duplicated values columns.
   3.drop_duplicated(inplace=True) is used to drop that duplicated values columns.
df['Date']:This assumes that 'Date' is a column in the Pandas DataFrame df that contains date or datetime strings.
pd.to_datetime():This is a Pandas function used to convert input into datetime.
It can handle various input formats (strings, timestamps, etc.) and convert them into datetime objects.
errors='coerce':This parameter specifies the action to take when encountering errors during conversion.
'coerce' is used here, which means that if an error occurs those problematic entries are set to NaT (Not a Time).


2. File Handling
-> Here two functions are created.

1st function is load_from_csv.
In this function a path is provided to create a file by using file operations.
File operations are used open the file and read the data from Clean_Covid_Data

2nd function is save_to_csv.
In this function a path is provided to create a file by using file operations.
File operations are used open the file and write the data into Clean_Covid_Data.csv


3.Analysis 
This code reads, cleans, and visualizes COVID-19 data, presenting key statistics and interactive charts on a Streamlit dashboard. It uses 'pandas' for data manipulation and 'matplotlib' for plotting, ensuring robust exception handling throughout.

--head(): Returns the first few rows of the DataFrame (df).
--groupby("Country/Region")["Confirmed"].sum(): Groups data by 'Country/Region' and calculates the sum of confirmed cases.
--reset_index(): Resets the index of the grouped DataFrame.
--sort_values("Confirmed", ascending=False): Sorts the DataFrame by confirmed cases in descending order.
--sum(): Calculates the total sum of values in specific columns ('Confirmed', 'Deaths', 'Recovered').

Streamlit Charts:
--st.bar_chart(): Displays bar charts for top and bottom countries/regions by confirmed cases.
--st.subheader(): Displays subheaders for different sections of the visualization.
--st.button(): Creates a button ("Show top/bottom 10 countries/states by cases") to trigger the display of top and bottom countries/regions by confirmed cases.
--used color='#FFC0CB' and color='#90EE90' for bar charts.
--st.button(): Creates a button ("Show top/bottom 10 countries/states by cases") to trigger the display of top and bottom countries/regions by confirmed cases.

4.Exception
DataCleaningError: user exception handling to catch and display errors related to data cleaning processes.


   