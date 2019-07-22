
#broker_url = 'amqp://localhost'
broker_url = 'redis://haproxy:6379/0'
result_backend = 'redis://haproxy:6379/1'
backend = 'redis://redis:haproxy/1'
task_serializer = 'json'
enable_utc = True
timezone = 'Europe/Rome'
