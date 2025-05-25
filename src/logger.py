# Importing necessary Python modules
import os  # For file/directory operations
import logging  # Python's built-in logging module
from datetime import datetime  # For timestamp handling

# Create a log filename with current timestamp
# Format: Month_Day_Year_Hour_Minute_Second.log (e.g., "06_15_2023_14_30_45.log")
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a full path for logs directory:
# - os.getcwd() gets current working directory
# - 'logs' is the subdirectory name
# - LOG_FILE is the filename created above
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)

# Create the logs directory if it doesn't exist:
# - exist_ok=True prevents errors if directory already exists
os.makedirs(logs_path, exist_ok=True)

# Create full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure Python's logging system:
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Where to write logs
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s ",
    # Format explanation:
    # %(asctime)s - Timestamp
    # %(lineno)d - Line number where log was called
    # %(name)s - Logger name
    # %(levelname)s - Log level (INFO, WARNING, etc.)
    # %(message)s - The actual log message
    level=logging.INFO  # Minimum level to capture (INFO and above)
)