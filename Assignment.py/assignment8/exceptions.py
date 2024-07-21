# exception.py(shweta)
import pandas as pd 

# Custom exception class for handling errors during data cleaning
class DataCleaningError(Exception):
    def __init__(self, message="Error during data cleaning"):
        self.message = message
        super().__init__(self.message)  # Call the parent class constructor with the provided message
