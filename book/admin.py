from django.contrib import admin
from book.models import Book, Category, Chapter, Volume


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'category', 'created', 'status', 'active')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ('name',)


