FROM python:3.11

WORKDIR /desafio-api

COPY ./requirements.txt /desafio-fastapi/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /desafio-fastapi/requirements.txt

COPY ./app /desafio-api/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
