from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
import sys


if __name__ == '__main__':
    logging.info("Starting the ML project")
    
    try:
        #data_ingestion_config=DataIngestionConfig(),
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("Coustom Exception")
        raise CustomException(e,sys)