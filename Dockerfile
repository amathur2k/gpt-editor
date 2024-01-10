FROM ubuntu:latest
WORKDIR /app
COPY requirements.txt .
RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y python3.9
RUN apt-get install -y python3-pip
RUN pip install -r requirements.txt
COPY run.py server.py ./
ARG OPENAI_API_KEY
EXPOSE 5000
CMD gunicorn --bind 0.0.0.0:$PORT server:app
