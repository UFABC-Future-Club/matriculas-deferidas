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

df = pd.read_excel (r'C:\Users\Windows\Downloads\turmas_e_docentes_2021_02.xlsx', header=None)

df.columns = ['CURSO', 'CÓDIGO DE TURMA', 'TURMA', 'TEORIA', 'PRÁTICA', 'Campus', 'TURNO', 'T-P-I', 'DOCENTE TEORIA', 'DOCENTE PRÁTICA']

df1 = df[['CÓDIGO DE TURMA', 'TURMA', 'TEORIA', 'PRÁTICA', 'TURNO', 'T-P-I', 'DOCENTE TEORIA', 'DOCENTE PRÁTICA']]

def insert_into_db(df1):
  for index, row in df1.iterrows():
    data = {
      'cod_turma': row['CÓDIGO DE TURMA'],
      'turma': row['TURMA'],
      'teoria': row['TEORIA'],
      'pratica': row['PRÁTICA'],
      'turno': row['TURNO'],
      't_p_i': row['T-P-I'],
      'prof_teoria': row['DOCENTE TEORIA'],
      'prof_pratica': row['DOCENTE PRÁTICA']
    }
    print(row['CÓDIGO DE TURMA'], '\n')

insert_into_db(df1)

#     x = mongo_col.insert_one(data)

# x = mongo_col.update_many({}, {"$set": {"new_field": "value"}}, upsert=False, array_filters=None)