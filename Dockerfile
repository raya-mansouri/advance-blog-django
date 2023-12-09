# syntax=docker/dockerfile:1
FROM python:3.10    
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY ./core/ /app

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]