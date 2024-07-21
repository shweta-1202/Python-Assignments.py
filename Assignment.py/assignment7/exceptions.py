# shweta exce_file

class DataCleaningError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
