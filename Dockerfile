FROM python:3
ARG HOST
ARG PORT
ARG LOGLEVEL

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir .

CMD python ./idarling_server.py -h $HOST -p $PORT --no-ssl -l $LOGLEVEL 
