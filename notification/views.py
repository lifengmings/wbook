import time
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from notification.models import Msg


@login_required
def updatemsg(request):
    while True:
        update_msg = Msg.objects.filter(is_read=False, target=request.user)
        data = dict()
        if update_msg:
            data['update_msg'] = str(update_msg)
            data['status'] = 'success'
            break
        else:
            time.sleep(13)
            data['status'] = 'error'
            break
    return JsonResponse(data)


@login_required
def set_read(request):
    msg = Msg.objects.get(pk=request.GET.get('pk'))
    msg.is_read = True
    msg.save()
    data = dict()
    data['status'] = 'success'
    return JsonResponse(data)