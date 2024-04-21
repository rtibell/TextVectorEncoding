#FROM python:3.11.9-alpine3.19
FROM python:3.11.4

# Make port 8090 available to the world outside this container
EXPOSE 8092

WORKDIR /app
RUN mkdir /root/.cache

RUN pip install --upgrade pip

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY RESTServer.py /app

ENV FLASK_APP=RESTServer.py

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8092"]
