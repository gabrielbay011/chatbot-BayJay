FROM python:3.12-slim

RUN apt-get update && apt-get install -y git
WORKDIR /app
COPY extract.py
ENTRYPOINT ["python", "extract.py"]