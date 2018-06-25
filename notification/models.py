from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import models


User = get_user_model()


class Msg(models.Model):
    '''content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')'''
    target = models.ForeignKey(User, on_delete=models.CASCADE)
    book_updated = models.ForeignKey('book.Book', on_delete=models.CASCADE)
    chapter_updated = models.ForeignKey('book.Chapter', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return '您收藏的{book}在{created}更新了{chapter}'.format(book=self.book_updated,
                                                         created=self.created,
                                                         chapter=self.chapter_updated)
