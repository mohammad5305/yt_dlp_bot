FROM python:3.12-alpine

WORKDIR /code

COPY ./requirements.txt .

RUN pip install -r requirements.txt

RUN apk add --no-cache ffmpeg

COPY . .

CMD ["python3", "main.py"]
