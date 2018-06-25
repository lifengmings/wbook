from django.shortcuts import render
from book.models import Book, Category


def home(request):
    categories = Category.objects.all()
    books_with_category = dict()
    for cate in categories:
        books = list(Book.objects.filter(active=True, category=cate))[:3]
        books_with_category['%s' % str(cate)] = books
    context = dict()
    context['book_commend'] = Book.objects.filter()
    context['books_with_category'] = books_with_category
    return render(request, 'home.html', context)

