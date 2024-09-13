FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY wait-for-it.sh /app/wait-for-it.sh
COPY . /app/

RUN chmod +x /app/wait-for-it.sh
RUN chmod +x /app/manage.py