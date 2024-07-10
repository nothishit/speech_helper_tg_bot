FROM python:3.12.4-slim-bullseye 

RUN apt-get update -y && apt-get upgrade -y && apt-get install ffmpeg -y

COPY app ./

COPY main.py ./

COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "main.py"]