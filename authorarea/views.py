from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from notification import signals
from authorarea.forms import CreateBookForm, UpdateBookForm, AddNewVolumeForm
from authorarea.utils import process_chapter_num
from book.models import Book, Chapter, Volume


def index(request):
    context = dict()
    return render(request, 'author_area_index.html', context)


def my_book_list(request):
    book_list = Book.objects.filter(author__pen_name=request.user.author.pen_name)
    context = dict()
    context['book_list'] = book_list
    return render(request, 'author_area/manage/manage_book_list.html', context)


@permission_required('book.add_book')
def create_book(request):
    if request.method == 'POST':
        createbookform = CreateBookForm(request.POST, request.FILES)
        if createbookform.is_valid():
            book = Book()
            book.category = createbookform.cleaned_data['category']
            book.name = createbookform.cleaned_data['name']
            book.cover = createbookform.cleaned_data['cover']
            book.summary = createbookform.cleaned_data['summary']
            book.author = request.user.author
            book.save()
            return redirect(reverse('author:update_book', args=[book.pk]))
        else:
            print(createbookform.errors)
    else:
        createbookform = CreateBookForm()
    context = dict()
    context['createbookform'] = createbookform
    return render(request, 'author_area/manage/create_book.html', context)


@permission_required('book.add_volume')
def add_new_volume_modal(request, pk):
    add_new_volume_form = AddNewVolumeForm(request.POST)
    data = {}
    if add_new_volume_form.is_valid():
        volume = Volume()
        volume.book_from = Book.objects.get(pk=pk)
        volume.name = add_new_volume_form.cleaned_data['name']
        volume.save()
        data['status'] = 'SUCCESS'
    else:
        data['status'] = 'ERROR'
    return JsonResponse(data)


@permission_required('book.add_volume')
def add_new_volume(request, pk):
    if request.method == 'POST':
        add_new_volume_form = AddNewVolumeForm(request.POST)
        if add_new_volume_form.is_valid():
            volume = Volume()
            volume.book_from = Book.objects.get(pk=pk)
            volume.name = add_new_volume_form.cleaned_data['name']
            volume.save()
            return redirect(request.get_full_path())
        else:
            print(add_new_volume_form.errors)
    else:
        add_new_volume_form = AddNewVolumeForm()
    context = dict()
    context['add_new_volume_form'] = add_new_volume_form
    return render(request, 'author_area/manage/add_new_volume.html', context)


@permission_required('book.add_chapter')
def update_book(request, pk):
    if request.method == 'POST':
        updatebookform = UpdateBookForm(request.POST)
        if updatebookform.is_valid():
            chapter = Chapter()
            chapter.book_from = Book.objects.get(pk=pk)
            chapter.volume_from = updatebookform.cleaned_data['volume_from']
            chapter.name = updatebookform.cleaned_data['name']
            chapter.contents = updatebookform.cleaned_data['content']
            word_num = float(process_chapter_num(updatebookform.cleaned_data['content']))
            chapter.word_num = word_num
            chapter.save()
            signals.book_updated_signal.send(
                sender=chapter.__class__,
                chapter=chapter,
                book=Book.objects.get(pk=pk),
            )
            return redirect(reverse('author:index'))
    else:
        updatebookform = UpdateBookForm()
        updatebookform.fields['volume_from'].queryset = Volume.objects.filter(book_from__pk=pk)
    context = dict()
    context['updatebookform'] = updatebookform
    context['book'] = Book.objects.get(pk=pk)
    return render(request, 'author_area/manage/update_book.html', context)



