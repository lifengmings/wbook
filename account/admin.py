from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from account.models import Author, Bookshelf

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('nickname', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('username', 'email', 'nickname', 'is_staff', 'is_active', 'is_superuser')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pen_name',)


@admin.register(Bookshelf)
class BookshelfAdmin(admin.ModelAdmin):
    list_display = ('owner', 'collection_books')



