from celery.schedules import crontab
from celery.task import periodic_task
from celery import shared_task


@shared_task
def some_task(): 
    """ A function that runs a task . """
    print('Hello')
