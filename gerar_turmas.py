import pandas as pd
from os.path import join, dirname
import os
from dotenv import load_dotenv
import pymongo

# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

# DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

# mongo_client = pymongo.MongoClient("mongodb+srv://root:" + DATABASE_PASSWORD + "@cluster0.hx5zk.mongodb.net/")
# mongo_db = mongo_client['app']
# mongo_col = mongo_db['matriculas']

df = pd.read_excel('./assets/turmas_e_docentes_2021_02.xlsx', header=None)

df.columns = ['CURSO', 'CÓDIGO DE TURMA', 'TURMA', 'TEORIA', 'PRÁTICA', 'Campus', 'TURNO', 'T-P-I', 'DOCENTE TEORIA', 'DOCENTE PRÁTICA']

df1 = df[['CÓDIGO DE TURMA', 'TURMA', 'TEORIA', 'PRÁTICA', 'TURNO', 'T-P-I', 'DOCENTE TEORIA', 'DOCENTE PRÁTICA']]

def insert_into_db(df1):
  for index, row in df1.iterrows():
    data = {
      'cod_turma': str(row['CÓDIGO DE TURMA']).replace('\xad', '-'),
      'turma': str(row['TURMA']).replace('\xad', '-'),
      'teoria': str(row['TEORIA']).replace('\xad', '-'),
      'pratica': str(row['PRÁTICA']).replace('\xad', '-'),
      'turno': str(row['TURNO']).replace('\xad', '-'),
      't_p_i': str(row['T-P-I']).replace('\xad', '-'),
      'prof_teoria': str(row['DOCENTE TEORIA']).replace('\xad', '-'),
      'prof_pratica': str(row['DOCENTE PRÁTICA']).replace('\xad', '-')
    }
    print(data)


insert_into_db(df1)

#     x = mongo_col.insert_one(data)

# x = mongo_col.update_many({}, {"$set": {"new_field": "value"}}, upsert=False, array_filters=None)