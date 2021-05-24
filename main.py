from fastapi import FastAPI
import settings.mongo_client

mongo_col = settings.mongo_client.mongo_col

app = FastAPI()

@app.get("/aulas/{ra}")
def listar_aulas(ra: int):
  aulas = []

  for data in mongo_col.find({"ra": ra}):
    aula = {
      'cod turma':data['cod_turma'],
      'turma': data['turma'],
      'prof_pratica': data['prof_pratica'],
      'prof_teoria': data['prof_teoria'],
      'teoria': data['teoria'].split(' ; '),
      'pratica': data['pratica'].split(' ; '), 
      'tpi' : data['tpi'],
      'turno' :data['turno']
    }

    aulas.append(aula)

  return {"aulas": aulas}
