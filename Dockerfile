FROM python:3
ARG PORT

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir .

CMD python ./idarling_server.py -h 127.0.0.1 -p 31013 --no-ssl -l DEBUG
