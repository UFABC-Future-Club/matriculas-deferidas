import tabula

def print_row(df):
  for index, row in df.iterrows():
    print(row['RA'], row['COD.TURMA'], row['TURMA'])

matricula_df = tabula.read_pdf("https://prograd.ufabc.edu.br/pdf/matriculas_pos_ajuste_2021_02.pdf")

print_row(matricula_df[0])
