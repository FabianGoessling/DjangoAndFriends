from django_unicorn.components import UnicornView
from crud.models import Book

class HelloWorldView(UnicornView):
    count = 0

    def add(self):
        self.count += 1

    def subtract(self):
        Book.objects.create(name="NEW", value=self.count)
        self.count -= 1