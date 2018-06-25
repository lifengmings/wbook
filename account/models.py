from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nickname = models.CharField("昵称", max_length=50)
    mugshot = models.ImageField("头像", upload_to='mugshot')

    def __str__(self):
        return self.username


class Bookshelf(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    collection_books = models.ForeignKey('book.Book', on_delete=models.CASCADE)


class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_author = models.BooleanField(default=False)
    pen_name = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.pen_name




