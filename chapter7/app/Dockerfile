FROM python:3.7.5-slim

RUN mkdir -p /var/app/flask_app
WORKDIR /var/app/flask_app
COPY requirements.txt /var/app/flask_app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /var/app/flask_app
ENV FLASK_APP ../app.py

CMD exec gunicorn -w 1 -b :8000 app:app --reload

