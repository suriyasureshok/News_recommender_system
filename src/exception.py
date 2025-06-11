import sys
from src.logger import logging

def get_error_message(error,error_detail:sys):
    """
    Function for getting error message from sys module.
    """
    exc_type,exc_value,exc_tb = error_detail.exc_info(error)
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        error_message = f"Error in file {file_name} at line {line_number} - {exc_value}"
    else:
        error_message = f"Error occured with message - {exc_value}"
    
    return error_message
class CustomException(Exception):
    """
    Base class for exceptions in this module.
    """
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message

    def __str__(self):
        return self.error_message
    
"""
Test code for the Custom Exception
"""
if __name__ == "__main__":
    try:
        a = 10
        b = a/0
    except Exception as e:
        logging.info("Error has been caught")
        raise CustomException(e,sys)