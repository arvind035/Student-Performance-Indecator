import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException
from src.logger import logging


class TrainingPipeline:
    def __init__(self):
        self.obj=DataIngestion()
        self.data_transformation=DataTransformation()
        self.modeltrainer=ModelTrainer()

    def start_training(self):
        try:
            logging.info("Training Started")
            train_data,test_data=self.obj.initiate_data_ingestion()
            train_arr,test_arr,_=self.data_transformation.initiate_data_transformation(train_data,test_data)
            print(self.modeltrainer.initiate_model_trainer(train_arr,test_arr))
            logging.info("Training Completed")
            
        except Exception as e:
            raise CustomException(e, sys)


