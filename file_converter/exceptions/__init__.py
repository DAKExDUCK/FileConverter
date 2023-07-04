from io import BytesIO


class ErrorConvertFile(Exception):
    """Exception raised for errors while converting file

    Attributes:
        file -- file which caused error
        message -- explanation of the error
    """

    def __init__(self, message_exc: str, message="Error while converting file"):
        self.message_exc = message_exc
        self.message = message
        super().__init__(self.message)
