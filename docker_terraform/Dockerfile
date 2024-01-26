FROM python:3.9.1

RUN pip install pgcli 

WORKDIR /app
COPY pipeline.py pipeline.py

ENTRYPOINT ["python", "pipeline.py"]