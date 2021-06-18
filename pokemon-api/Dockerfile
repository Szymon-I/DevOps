FROM python:3.9-slim

RUN mkdir /app 
COPY poetry.lock pyproject.toml /app/
WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.main.app:app"]
