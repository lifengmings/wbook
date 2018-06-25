from django.dispatch import receiver, Signal

from book.models import Chapter

update_book_word_num = Signal(providing_args=["chapter"])


@receiver(update_book_word_num, sender=Chapter)
def update_book_msg(sender, **kwargs):
    chapter = kwargs['chapter']
    book = kwargs['book']
    book.word_num = book.word_num + chapter.word_num
    book.save()