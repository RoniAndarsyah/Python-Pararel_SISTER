from celery import Celery
import time
app = Celery('tugas',broker='amqp://guest@localhost//')

@app.task
def longtime_add(x, y):
    print('tugas dimulai')
    # sleep 5 detik
    time.sleep(5)
    print('tugas telah selesai')
    return x + y
    