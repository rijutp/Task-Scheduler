from celery import Celery
import requests
 
celery = Celery('task')
celery.config_from_object('celeryconfig')
 
@celery.task
def add(x, y):
    return x + y

@celery.task
def mad(message):
    # r=requests.get("http://localhost:5000/publish?message=+message")
    # r.get()
    r=message
    requests.get("http://localhost:5000/publish?message="+r)