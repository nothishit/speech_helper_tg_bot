FROM python:3.12.4-slim-bullseye 

RUN apt-get update -y && apt-get upgrade -y && apt-get install ffmpeg -y

WORKDIR /app

COPY app src

COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "/app/src/main.py"]