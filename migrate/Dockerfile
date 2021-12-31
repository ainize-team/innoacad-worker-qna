FROM    python:3.8.12

RUN pip install --upgrade pip

WORKDIR /app

COPY    requirements.txt .
RUN pip install -r requirements.txt

COPY    . .

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN pip install -r requirements.txt
RUN chmod +x db_migrate.sh

ENTRYPOINT ["/bin/bash", "./db_migrate.sh"]
