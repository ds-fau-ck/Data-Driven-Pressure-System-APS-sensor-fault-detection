from sensor.configuration.mongo_db_connection import MongoDBClient  
if __name__=="__main__":
    mongodb_client=MongoDBClient()
    print("Collection Names:",mongodb_client.Database.list_collection_names())
  