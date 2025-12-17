from sensor.configuration.mongo_db_connection import MongoDBClient 
from sensor.exception import SensorException
import sys
from sensor.logger import logging
#from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeline
import os

def test_exception():
    try:
        logging.info("We are dividing 1 by zero")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)

if __name__=="__main__":
    
    train_pipeline=TrainPipeline()
    train_pipeline.run_pipeline()
    #training_pipeline_config=TrainingPipelineConfig()
    #data_ingestion_config=DataIngestionConfig(training_pipeline_config=training_pipeline_config)
    #print(data_ingestion_config.__dict__)
    #mongodb_client=MongoDBClient()
    #print("Collection Names:",mongodb_client.Database.list_collection_names())
  