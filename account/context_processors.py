from authorarea.forms import AddNewVolumeForm
from book.models import Category
from notification.models import Msg
from .forms import LoginForm


def login_modal_form(request):
    return {'login_modal_form': LoginForm()}


def add_new_volume_form(request):
    return {'add_new_volume_form': AddNewVolumeForm()}


def categories(request):
    return {'categories': Category.objects.filter()}


def update_msg(request):
    if request.user.is_authenticated:
        update_msg = Msg.objects.filter(is_read=False, target=request.user)
    else:
        update_msg = None
    return {'update_msg': update_msg}
