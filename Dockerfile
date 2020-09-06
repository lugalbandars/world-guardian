FROM python:3.8.5-slim-buster
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 5000
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . .
ENTRYPOINT ["gunicorn"]
CMD ["-c", "gunicorn.conf.py", "main:app"]