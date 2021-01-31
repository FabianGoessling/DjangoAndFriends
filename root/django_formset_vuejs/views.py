from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from . import models
from . import forms
from . import serializers
import json


def bt(request):
    return render(request, 'django_formset_vuejs/backtest_template.html')


def rest_get_request(request):
    return render(request, 'django_formset_vuejs/api_call.html')

def author_books_formset(request):
    # Get the current user
    user = request.user

    # give an id to an author
    if user.is_anonymous:
        author, _ = models.AuthorContainer.objects.get_or_create(
            id=request.session.get('author_id', None))
        request.session['author_id'] = author.id
        request.session.save()

    # load the author container object
    author =  None# models.AuthorContainer.objects.get(id=request.session['author_id'])

    if author is None:
        author = models.AuthorContainer()


    if request.method == 'POST':
        formset = forms.AuthorsFormset(request.POST or None,
                                       request.FILES,
                                       instance=author)
        with transaction.atomic():
            if formset.is_valid():
                obj = formset.save(commit=False)
                for deleted in formset.deleted_objects:
                    deleted.delete()
                for form in obj:
                    form.author_container = author
                    form.save()
                obj = formset.save()
                messages.success(request, 'Saved successfully!')
                return redirect('author')
            else:
                messages.warning(request, 'Please try again!')
    else:
        formset = forms.AuthorsFormset(instance=author)
        ts = serializers.AuthorContainerSerializer(author)
        print(ts.data)
      #  ts = serializers.AuthorSerializer(author.author_set.all()[0])
      #  print(ts.data)

    return render(request, 'django_formset_vuejs/author.html', {
        'parent': author,
        'authors': json.dumps(ts.data)})

        

