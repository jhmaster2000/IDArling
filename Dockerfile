FROM python:3
ARG PORT

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir .

CMD python ./idarling_server.py -p $PORT -l DEBUG
