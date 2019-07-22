from celery import Celery
import celeryconfig


try:
    app = Celery('tasks')
    app.config_from_object(celeryconfig)
except Exception as e:
    sys.exit(5)
    # print(str(e))

@app.task
def add(x, y):
    return x + y
