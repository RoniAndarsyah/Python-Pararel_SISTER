###
## addTask.py :Executing a simple task
###

from celery import Celery

app = Celery('addTask',broker='amqp://guest@localhost:5672//')

@app.task
def add(x, y):
    return x + y
