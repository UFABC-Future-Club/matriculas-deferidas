import os
from os.path import join, dirname
from dotenv import load_dotenv
import tabula
import pandas as pd
import pymongo

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

mongo_client = pymongo.MongoClient("mongodb+srv://root:" + DATABASE_PASSWORD + "@cluster0.hx5zk.mongodb.net/")
mongo_db = mongo_client['app']
mongo_col = mongo_db['matriculas']

def insert_into_db(df):
  for index, row in df.iterrows():
    data = {
      'ra': row['RA'],
      'cod_turma': row['COD.TURMA'],
      'turma': row['TURMA']
    }

    x = mongo_col.insert_one(data)

matricula_df = tabula.read_pdf("https://prograd.ufabc.edu.br/pdf/matriculas_pos_ajuste_2021_02.pdf", pages='all')

result = pd.concat(matricula_df)

insert_into_db(result)