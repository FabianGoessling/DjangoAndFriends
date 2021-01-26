from celery.schedules import crontab
from celery.task import periodic_task
from celery import shared_task


@shared_task
def some_task():
    print('Hello')
