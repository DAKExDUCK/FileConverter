

class ErrorConvertFile(Exception):
    """Exception raised for errors while converting file

    Attributes:
        file -- file which caused error
        message -- explanation of the error
    """

    def __init__(self, message: str):
        self.message = f"Error while converting file - {message}"
        super().__init__(self.message)
