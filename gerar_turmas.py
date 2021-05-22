import tabula
import pandas as pd
import pymongo


def insert_into_db(df):
  for index, row in df.iterrows():
    data = {
      'cod_turma': row['CÓDIGO DE\rTURMA'],
      'turma': row['TURMA'],
      'teoria': row['SISTEMA'],
      'pratica': row['TEORIA'],
      'campus': row['Campus'],
      'turno': row['turno'],
      't_p_i': row['t-p-i'],
      'prof_teoria': row['DOCENTE TEORIA'],
      'prof_pratica': row['DOCENTE PRÁTICA']
    }
    print(row['SISTEMA'],
      "\n")

turmas_df = tabula.read_pdf("https://prograd.ufabc.edu.br/pdf/ajuste_2021.2_turmas_ofertadas.pdf", pages='all')

resultado = pd.concat(turmas_df)

insert_into_db(resultado)