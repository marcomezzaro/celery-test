FROM redis:5.0.5-alpine
RUN mkdir -p /data
COPY redis.conf /usr/local/etc/redis/redis.conf
WORKDIR /data
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]