import numpy as np
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def demo(request):
    if request.method == 'POST':
        print(request.POST)
        color = request.POST.get('dataset')
        number = int(request.POST.get('label'))
        demographics_ctx = 'aha'
        print(color)
        print(number)

        response = {
            "color": color,
            "msg": 'hallo',
            "labels": list(np.linspace(1, number, number)),
            "data": list(np.random.randn(number)),
        }

        return JsonResponse(response)

    return render(request, 'visualization_chartjs/barchart.html', {})
