import sys
from typing import Optional
import os
import numpy as np
import pandas as pd
import json
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant.database import DATABASE_NAME
from sensor.exception import SensorException

from sensor.logger import logging
from pandas import DataFrame
class SensorData:
    """
    This class help to export entire mongo db record as pandas dataframe
    """

    def __init__(self):
        """
        """
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)

        except Exception as e:
            raise SensorException(e, sys)


    def save_csv_file(self,file_path ,collection_name: str, database_name: Optional[str] = None):
        try:
            data_frame=pd.read_csv(file_path)
            data_frame.reset_index(drop=True, inplace=True)
            records = list(json.loads(data_frame.T.to_json()).values())
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            collection.insert_many(records)
            return len(records)
        except Exception as e:
            raise SensorException(e, sys)
    def export_data_into_feature_store(self)->DataFrame:
        """
        Export mongo db collection record as pandas dataframe into feature store"""
        try:
            logging.info("Exporting data from mongodb to feature store")
            sensor_data=SensorData()
            dataframe=sensor_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
                        #sensor_data_frame = self.export_collection_as_dataframe(collection_name="sensor")
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            # Creating folder
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False, header=True)
            return dataframe
            #return sensor_data_frame
        except Exception as e:
            raise SensorException(e, sys)

    def export_collection_as_dataframe(
        self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            """
            export entire collectin as dataframe:
            return pd.DataFrame of collection
            """
            if database_name is None:
                collection = self.mongo_client.Database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
                print("Collection Name:",collection_name)
            df = pd.DataFrame(list(collection.find()))
            print("Columns in df:",df.columns.to_list())

            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            df.replace({"na": np.nan}, inplace=True)

            return df

        except Exception as e:
            raise SensorException(e, sys)