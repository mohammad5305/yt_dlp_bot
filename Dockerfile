FROM python:3.12-alpine

WORKDIR /code

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
