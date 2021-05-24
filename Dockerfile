FROM python:3.7

RUN mkdir /app

COPY ./app /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
