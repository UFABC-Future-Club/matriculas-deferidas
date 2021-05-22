import pandas as pd

df = pd.read_excel (r'C:\Users\Windows\Downloads\turmas_e_docentes_2021_02.xlsx', header=None)

df.columns = ['CURSO', 'CÓDIGO DE TURMA', 'TURMA', 'SISTEMA', 'TEORIA', 'Campus', 'turno', 't­p­i', 'DOCENTE TEORIA', 'DOCENTE PRÁTICA']

df1 = df[['CÓDIGO DE TURMA', 'TURMA', 'SISTEMA', 'TEORIA', 'Campus', 'turno', 't­p­i', 'DOCENTE TEORIA', 'DOCENTE PRÁTICA']]