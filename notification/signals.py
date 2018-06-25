from django.dispatch import receiver, Signal
from account.models import Bookshelf
from notification.models import Msg
from book.models import Chapter

book_updated_signal = Signal(providing_args=["chapter"])


@receiver(book_updated_signal, sender=Chapter)
def update_book_msg(sender, **kwargs):
    chapter = kwargs['chapter']
    book = kwargs['book']
    bookshelf = Bookshelf.objects.filter(collection_books=book)
    for i in bookshelf:
        msg, created = Msg.objects.get_or_create(book_updated=book, chapter_updated=chapter, target=i.owner)
        if not created:
            # 不是第一次更新章节
            msg.chapter_updated = chapter
        msg.save()

    # 更新作品总字数
    book.word_num = book.word_num + chapter.word_num
    book.save()
