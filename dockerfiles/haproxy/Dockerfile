FROM alpine:3.9

LABEL Author "Marco Mezzaro"

RUN apk update && \
    apk add haproxy && \
    mkdir -p /etc/haproxy

COPY haproxy.cfg /etc/haproxy/haproxy.cfg

CMD haproxy -f /etc/haproxy/haproxy.cfg