from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=30)
    value = models.FloatField(null=True)

    def __str__(self):
        return f'Book {self.name}'

class Site(models.Model):
    page = models.CharField(max_length=30)
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE)

    def __str__(self):
        return f'Site {self.page}'



