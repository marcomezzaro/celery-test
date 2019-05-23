This is a simple Celery app that uses Redis as a broker.

It's intended to track down the source of https://github.com/andymccurdy/redis-py/issues/1140


The Celery daemon is being run with the command: `celery -A tasks worker --loglevel=debug`

To enqueue a new task, run `python add_task.py`
