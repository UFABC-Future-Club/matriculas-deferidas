import pandas as pd
import pymongo
import settings.mongo_client

mongo_col = settings.mongo_client.mongo_col

df = pd.read_excel('../assets/turmas_e_docentes_2021_02.xlsx', header=None)

df.columns = ['CURSO', 'CÓDIGO DE TURMA', 'TURMA', 'TEORIA', 'PRÁTICA', 'Campus', 'TURNO', 'T-P-I', 'DOCENTE TEORIA', 'DOCENTE PRÁTICA']

df1 = df[['CÓDIGO DE TURMA', 'TURMA', 'TEORIA', 'PRÁTICA', 'TURNO', 'T-P-I', 'DOCENTE TEORIA', 'DOCENTE PRÁTICA']]

def insert_into_db(df1):
  for index, row in df1.iterrows():
    
    cod_turma = str(row['CÓDIGO DE TURMA']).replace('\xad', '-')

    data = {
      'teoria': str(row['TEORIA']).replace('\xad', '-').replace('nan', ''),
      'pratica': str(row['PRÁTICA']).replace('\xad', '-').replace('nan', ''),
      'turno': str(row['TURNO']).replace('\xad', '-').replace('nan', ''),
      'tpi': str(row['T-P-I']).replace('\xad', '-').replace('nan', ''),
      'prof_teoria': str(row['DOCENTE TEORIA']).replace('\xad', '-').replace('nan', ''),
      'prof_pratica': str(row['DOCENTE PRÁTICA']).replace('\xad', '-').replace('nan', '')
    }
    x = mongo_col.update_many({"cod_turma": cod_turma}, {"$set": data}, upsert=True, array_filters=None)
    print('atualizando:', cod_turma, index)


insert_into_db(df1)