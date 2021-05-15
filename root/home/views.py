import numpy as np
from django.apps import apps
from django.contrib import messages
from django.http.request import HttpRequest
from django.shortcuts import render
from prefect import Client, Flow, task

from .models import User


def home(request: HttpRequest):
    return render(request, "home/index.html", {'apps': apps.get_app_configs()})


def prefect_flow(request: HttpRequest):
    #    client = Client()
    #    client.create_project(project_name="Hello, World!")

    @task
    def say_hello():
        name = 'User' + str(np.random.rand())
        print(name)
        app, _ = User.objects.get_or_create(name=name)
        print(app)

    flow = Flow("hello2", tasks=[say_hello])
    flow.register(project_name="Hello, World!")

    messages.success(request, 'Prefect Flow completed!')
    return render(request, 'home/message_page.html', )


def prefect_flow_run(request: HttpRequest): 
    c = Client()
    c.create_flow_run(flow_id="e41a168a-da69-4aef-8adf-699aef230e70")
    return render(request, 'home/message_page.html')


def vuetest(request: HttpRequest):
    context = dict()
    return render(request=request, context=context)
