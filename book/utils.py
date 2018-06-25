import redis
from django.conf import settings

r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DB)


def get_click_num(request, book_obj):
    key = "%s_click" % book_obj.pk
    if not request.COOKIES.get(key):
        click_num = r.incr('book:{}:click'.format(book_obj.pk))
        r.zincrby('click_ranking', book_obj.pk, 1)
    else:
        click_num = r.get('book:{}:click'.format(book_obj.pk))
    return click_num, key




