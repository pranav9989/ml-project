import os  # For file/directory operations
import sys  # For system-specific parameters and functions
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.exception import CustomException  # Custom exception handler
from src.logger import logging  # Custom logging configuration
import pandas as pd  # For data manipulation
from sklearn.model_selection import train_test_split  # For splitting data
from dataclasses import dataclass  # For creating configuration class
from src.components.data_transformation import DataTransformation, DataTransformationConfig

@dataclass
class DataIngestionConfig:
    """
    Configuration class for data ingestion paths.
    Uses @dataclass decorator to automatically generate special methods.
    
    Attributes:
        train_data_path (str): Path to save training data (default: 'artifact/train.csv')
        test_data_path (str): Path to save testing data (default: 'artifact/test.csv')
        raw_data_path (str): Path to save raw data (default: 'artifact/raw.csv')
    """
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")

class DataIngestion:
    """
    Data Ingestion component responsible for:
    - Loading source data
    - Splitting into train/test sets
    - Saving processed data to specified paths
    
    Methods:
        __init__(): Initializes configuration
        initiate_data_ingestion(): Executes the data ingestion pipeline
    """
    
    def __init__(self):
        """Initializes DataIngestion with configuration settings"""
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        """
        Main method to execute data ingestion process:
        1. Reads source data
        2. Saves raw data copy
        3. Splits into train/test sets
        4. Saves processed data
        
        Returns:
            tuple: (train_data_path, test_data_path)
            
        Raises:
            CustomeException: If any error occurs during ingestion
        """
        logging.info("Entered the data ingestion method or component")
        try:
            # Step 1: Read source data
            df = pd.read_csv("d:/ml projectt/src/notebook/data/stud.csv")
            logging.info("Read the dataset")

            # Step 2: Create directory if not exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Step 3: Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            # Step 4: Split data
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Step 5: Save processed data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of the data completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            # Handle and log errors using custom exception
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    # When run directly, execute the data ingestion pipeline
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)