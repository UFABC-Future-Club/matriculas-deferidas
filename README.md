# API UFABC

![Logo UFABC](docs/logo-ufabc.png)

Essa API tem como objetivo prover informações relacionadas a Universidade Federal do ABC.

## Funcionalidades
- [x] Disciplinas que estão sendo cursadas por RA;
- [ ] Fórum de dúvidas;
- [ ] Horário dos fretados;
- [ ] Cardápio RU;
- [ ] ...em breve;

### Disciplinas por RA
Requisição do tipo GET que retorna um vetor com os detalhes como nome, horários, docente, TPI e etc das disciplinas que estão sendo cursadas pelo RA requerido.

#### Exemplo:
###### Requisição:
```http
GET /aulas/<ra> HTTP/1.1
```

###### Retorno:
```json
{
  "aulas": [
    {
      "cod turma": "<código da turma>",
      "turma": "<nome da turma>",
      "prof_pratica": "<nome do professor da prática>",
      "prof_teoria": "<nome do professor da teoria>",
      "teoria": [
        "<horário e quinzena da(s) aula(s) teórica(s)>",
        "<horário e quinzena da(s) aula(s) teórica(s)>"
      ],
      "pratica": [
        "<horário e quinzena da(s) aula(s) prática(s)>"
      ],
      "tpi": "<T-P-I>",
      "turno": "<diurno ou noturno>"
    }
  ]
} 
```


