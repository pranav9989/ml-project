# Importing required modules
import sys  # Provides access to system-specific parameters and functions
from src.logger import logging  # Importing your custom logger module

def error_msg_detail(error, error_detail):
    """
    Constructs a detailed error message including filename, line number, and error.
    
    Args:
        error: The error/exception object
        error_detail: Contains execution info from sys.exc_info()
    
    Returns:
        str: Formatted error message with debugging details
    """
    # exc_info() returns (type, value, traceback)
    # We only need the traceback (exc_tb) to get execution details
    _, _, exc_tb = error_detail.exc_info()
    
    # Get the filename where error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Format error message with script name, line number, and error
    error_message = "Error occurred in python script name [{}] at line number [{}] error message [{}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    """
    Custom exception class that enhances standard exceptions with:
    - Detailed error messages
    - Automatic logging capability
    - File and line number context
    
    Inherits from Python's base Exception class
    """
    def __init__(self, error_message, error_detail):
        """
        Initialize the custom exception with enhanced error details
        
        Args:
            error_message: The error description
            error_detail: System execution info from sys.exc_info()
        """
        # Initialize parent Exception class
        super().__init__(error_message)
        
        # Generate detailed error message
        self.error_message = error_msg_detail(error_message, error_detail=error_detail)
        
        # Log the error automatically when exception occurs
        logging.error(self.error_message)

    def __str__(self):
        """
        String representation of the exception
        Returns the detailed error message when printed
        """
        return self.error_message