from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.template.loader import render_to_string

from .forms import BookForm, site_set, SiteSetHelper
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
        return render(request, "crud/jexcel_input.html")
    if request.method == "POST":
        response = {"0": ["MP", "AA"], "1": ["fffff", "bbb"]}
    return JsonResponse(response)


def dynamic_form(request):
    """Returns a dynamic form page

    Args:
        request (HttpRequest): [description]

    Returns:
        [type]: [description]
    """
    context = {}
    if request.method == "POST":
        bookform = BookForm(request.POST)
        if bookform.is_valid():
            book = bookform.save()
            context["bookform"] = "success"
            sitesetf = site_set(1)(request.POST, instance=book)
            if sitesetf.is_valid():
                sitesetf.save()
                context["form_is_valid"] = True
            else:
                context["form_is_valid"] = False

        all_books = Book.objects.all()
        context["book_table"] = render_to_string(
            "crud/partials/table_partial.html", {"book_list": all_books}, request
        )
        return JsonResponse(context)
    else:
        book = Book.objects.first()
        context["form"] = BookForm(
            initial={"name": book.name, "value": book.value})

        # fill the formset with existing sites
        context["siteset"] = site_set(extra=len(book.site_set.all()))(
            initial=[{"page": site.page} for site in book.site_set.all()]
        )
        context["sitesetHelper"] = SiteSetHelper()

        all_books = Book.objects.all()
        context["book_list"] = all_books
        return render(request, "crud/form_page.html", context=context)
