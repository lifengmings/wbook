from django.contrib import admin
from notification.models import Msg


@admin.register(Msg)
class UpdateMsgAdmin(admin.ModelAdmin):
    list_display = ('book_updated', 'chapter_updated', 'created', 'target', 'is_read')
