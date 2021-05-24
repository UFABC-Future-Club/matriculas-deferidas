import tabula
import pandas as pd
import settings.mongo_client

mongo_col = settings.mongo_client.mongo_col

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