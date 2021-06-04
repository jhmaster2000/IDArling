FROM python:3
ARG PORT

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir .

CMD python ./idarling_server.py -h 192.168.1.1 -p 31013 --no-ssl -l DEBUG
