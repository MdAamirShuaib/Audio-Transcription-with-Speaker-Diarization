FROM python:3.10.4
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "main:app", "--workers","3","--worker-class" ,"uvicorn.workers.UvicornWorker","--bind","0.0.0.0:8000", "--reload", "--timeout","1000000000"]