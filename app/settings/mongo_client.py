import os
from os.path import join, dirname
from dotenv import load_dotenv
import pymongo

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

mongo_client = pymongo.MongoClient("mongodb+srv://root:" + DATABASE_PASSWORD + "@cluster0.hx5zk.mongodb.net/")
mongo_db = mongo_client['app']
mongo_col = mongo_db['matriculas']