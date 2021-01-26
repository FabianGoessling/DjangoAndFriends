from home.models import Books

# queryset.py
from django_unicorn.components import UnicornView

class TestFormView(UnicornView):
    books = Books.objects.none()

    def hydrate(self):
        # Using `hydrate` is the best way to make sure that QuerySets
        # are re-queried every time the component is loaded
        print('hydrated')
        self.books = Books.objects.all().order_by("-id")[:5]

    def save(self):
        pass