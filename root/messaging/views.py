from django.contrib import messages
from django.shortcuts import render


def message_tester(request):
    messages.success(request, 'Hello World')
    return render(request, 'messaging/message_page.html')
