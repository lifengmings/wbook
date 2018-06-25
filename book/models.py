from django.contrib.auth.models import User
from django.db import models
from account.models import Author


class Category(models.Model):
    CATEGORY_CHOICES = (
        ('仙侠', '仙侠'),
        ('玄幻', '玄幻'),
        ('都市', '都市'),
        ('科幻', '科幻'),
        ('历史', '历史'),
        ('游戏', '游戏'),
        ('灵异', '灵异'),
        ('武侠', '武侠'),
    )
    name = models.CharField(max_length=10, verbose_name='分类', choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Book(models.Model):

    STATUS_CHOICES = (
        ('连载', '连载'),
        ('完本', '完本'),
    )
    name = models.CharField(max_length=25, verbose_name='书名', unique=True)
    author = models.ForeignKey(Author, verbose_name='作者', on_delete=models.CASCADE)
    word_num = models.FloatField(default=0)
    cover = models.ImageField(upload_to='cover', verbose_name='封面', blank=True, default='')
    summary = models.TextField(verbose_name='简介')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    status = models.CharField(max_length=10, verbose_name='状态', choices=STATUS_CHOICES, default='连载')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Volume(models.Model):
    name = models.CharField(max_length=20, verbose_name='卷名', unique=False)
    book_from = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=20, verbose_name='章节')
    contents = models.TextField(verbose_name='内容')
    created = models.DateTimeField(auto_now_add=True)
    word_num = models.FloatField(default=0)
    book_from = models.ForeignKey(Book, on_delete=models.CASCADE)
    volume_from = models.ForeignKey(Volume, on_delete=models.CASCADE)

    def __str__(self):
        return self.name





