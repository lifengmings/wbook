from django import template

from account.models import Bookshelf
from book.models import Book

register = template.Library()


@register.simple_tag(takes_context=True)
def get_collect_status(context, pk):
    book = Book.objects.get(pk=pk)
    user = context['user']
    if not user.is_authenticated:
        return ''
    if Bookshelf.objects.filter(owner=user, collection_books=book).exists():
        return 'active'
    else:
        return ''
