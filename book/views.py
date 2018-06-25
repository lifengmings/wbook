from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from account.models import Bookshelf
from book.models import Book, Category, Chapter
from book.utils import get_click_num, r


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    volumes = book.volume_set.all()
    vol = dict()
    for volume in volumes:
        chapters = list(book.chapter_set.filter(volume_from=volume))
        vol['%s' % volume] = chapters
    click_num, key = get_click_num(request, book)
    context = dict()
    context['book'] = book
    context['vol'] = vol
    context['click_num'] = int(click_num)
    response = render(request, 'book/book_detail.html', context)
    response.set_cookie(key, 'true', max_age=21600)  # 6小时过期
    return response


def read_page(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    book = Book.objects.get(chapter=chapter)
    context = dict()
    context['chapter'] = chapter
    context['previous'] = Chapter.objects.filter(book_from__name=book.name, created__lt=chapter.created).last()
    context['next'] = Chapter.objects.filter(book_from__name=book.name, created__gt=chapter.created).first()
    return render(request, 'book/read_page.html', context)


def classify_x(request, name):
    book_list = Book.objects.filter(category__name=name)
    categories = Category.objects.all()
    context = dict()
    context['book_list'] = book_list
    context['categories'] = categories
    context['book_commend'] = book_list
    return render(request, 'classify/classify_x.html', context)


def join_bookshelf(request):
    data = dict()
    if not request.user.is_authenticated:
        data['status'] = 'ERROR'
        data['code'] = 400
        return JsonResponse(data)

    pk = request.GET.get('pk')
    if request.GET.get('is_collect') == 'true':
        # 收藏
        book_shelf, created = Bookshelf.objects.get_or_create(owner=request.user, collection_books=Book.objects.get(pk=pk))
        if created:
            book_shelf.save()
            data['action'] = '1'
            data['status'] = 'SUCCESS'
            return JsonResponse(data)
    # 取消收藏
    if Bookshelf.objects.filter(owner=request.user, collection_books=Book.objects.get(pk=pk)).exists():
        bookshelf = Bookshelf.objects.get(owner=request.user, collection_books=Book.objects.get(pk=pk))
        bookshelf.delete()
        data['action'] = '0'
        data['status'] = 'SUCCESS'
        return JsonResponse(data)


def click_rank(request):
    click_ranking = r.zrange('click_ranking', 0, -1, desc=True)[:7]
    click_ranking_ids = [int(pk) for pk in click_ranking]
    most_click = list(Book.objects.filter(
        id__in=click_ranking_ids))
    most_click.sort(key=lambda x: click_ranking_ids.index(x.id))
    context = dict()
    context['most_click'] = most_click
    return render(request, 'book/click_ranking.html', context)


