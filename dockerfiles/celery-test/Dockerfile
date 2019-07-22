FROM alpine:3.9

LABEL Author "Marco Mezzaro"

RUN apk update && \
    apk add python3 py3-pip

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt
WORKDIR /opt
CMD celery -A tasks worker --loglevel=debug