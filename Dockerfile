FROM python:3.12.4-slim-bullseye 

RUN sudo apt-get update && apt-get upgrade && apt-get install ffmpeg

COPY app ./

WORKDIR /app 

COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "main.py"]