from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import BookForm, SiteSet, sitesetHelper
from .models import Book


@require_http_methods(["GET", "POST"])
def jexcel_input(request):
    """Returns the basis page

    Args:
        request ([type]): request

    Returns:
        [type]: [description]
    """
    if request.method == "GET":
        return render(request, "jexcel_crud/jexcel.html")
    if request.method == "POST":
        response = {"0": ["MP", "AA"], "1": ["fffff", "bbb"]}
    return JsonResponse(response)


def dynamic_form(request):
    """Returns a dynamic form page

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    context = {}
    if request.method == "POST":
        bookform = BookForm(request.POST)
        if bookform.is_valid():
            book = bookform.save()
            context["bookform"] = "success"
            sitesetf = SiteSet(1)(request.POST, instance=book)
            if sitesetf.is_valid():
                sitesetf.save()
                context["sitesetf"] = "success"
        return JsonResponse(context)
    else:
        book = Book.objects.first()
        context["form"] = BookForm(initial={"name": book.name, "value": book.value})

        context["siteset"] = SiteSet(extra=len(book.site_set.all()))(
            initial=[{"page": site.page} for site in book.site_set.all()]
        )
        context["sitesetHelper"] = sitesetHelper()
        return render(request, "jexcel_crud/form_page.html", context=context)
