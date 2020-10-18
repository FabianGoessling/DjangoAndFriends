from django import forms
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class ColorForm(forms.Form):
    color = forms.CharField()


ColorFormSet = formset_factory(ColorForm, extra=1)
# we'll dynamically create the elements, no need for any forms


from django.shortcuts import render, redirect
from django.views import generic

from .forms import (
    BookFormset,
    BookModelFormset,
    BookModelForm,
    AuthorFormset
)
from .models import Book, Author


def create_book_normal(request):
    template_name = 'store/create_normal.html'
    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = BookFormset(request.GET or None)
    elif request.method == 'POST':
        formset = BookFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data.get('name')
                # save book instance
                if name:
                    Book(name=name).save()
            return redirect('store:book_list')

    return render(request, template_name, {
        'formset': formset,  # noqa
        'heading': heading_message,
    })


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'store/list.html'


def create_book_model_form(request):
    template_name = 'store/create_normal.html'
    heading_message = 'Model Formset Demo'
    if request.method == 'GET':
        formset = BookModelFormset(queryset=Book.objects.none())
    elif request.method == 'POST':
        formset = BookModelFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # only save if name is present
                if form.cleaned_data.get('name'):
                    form.save()
            return redirect('polls:book_list')

    return render(request, template_name, {
        'formset': formset,  # noqa
        'heading': heading_message,
    })


def create_book_with_authors(request):
    template_name = 'polls/create_with_author.html'
    if request.method == 'GET':
        bookform = BookModelForm(request.GET or None)
        formset = AuthorFormset(queryset=Author.objects.none())
    elif request.method == 'POST':
        bookform = BookModelForm(request.POST)
        formset = AuthorFormset(request.POST)
        if bookform.is_valid() and formset.is_valid():
            # first save this book, as its reference will be used in `Author`
            book = bookform.save()
            for form in formset:
                # so that `book` instance can be attached.
                author = form.save(commit=False)
                author.book = book
                author.save()
            return redirect('polls:book_list')
    return render(request, template_name, {
        'bookform': bookform,  # noqa
        'formset': formset,  # noqa
    })


def myview(request):
    print(request)
    if request.method == "POST":
        formset = ColorFormSet(request.POST)
        formset.is_valid()
        print(formset)
        for form in formset.forms:
            form.is_valid()
            print(form.cleaned_data)
    else:
        formset = ColorFormSet()
    return render(request, 'polls/formtest.html', {'formset': formset})
