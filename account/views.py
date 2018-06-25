from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from account.forms import LoginForm, AuthorRegisterForm, RegisterForm
from account.models import Author
from django.contrib.auth import get_user_model
from .models import Bookshelf


User = get_user_model()


def user_register(request):
    if request.method == 'POST':
        user_reg_form = RegisterForm(request.POST)
        if user_reg_form.is_valid():
            cd = user_reg_form.cleaned_data
            username = cd['username']
            email = cd['email']
            password = cd['password']
            user = User.objects.create_user(username, email, password)
            user.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from', '/'))
    else:
        user_reg_form = RegisterForm()

    context = dict()
    context['user_reg_form'] = user_reg_form
    return render(request, 'account/user_register.html', context)


def login(request):
    login_form = LoginForm(request.POST)
    data = {}
    if login_form.is_valid():
        user = login_form.cleaned_data['user']
        auth.login(request, user)
        data['status'] = 'SUCCESS'

    else:
        data['status'] = 'ERROR'
    return JsonResponse(data)


def user_logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def author_register(request):
    if request.method == 'POST':
        reg_form = AuthorRegisterForm(request.POST)
        if reg_form.is_valid():
            cd = reg_form.cleaned_data
            pen_name = cd['pen_name']
            user = User.objects.get(username=request.user.username)
            author = Author.objects.create(user=user, pen_name=pen_name, is_author=True)
            author.save()
            g = Group.objects.get(name='author')
            user.groups.add(g)
            return redirect(request.GET.get('from', '/'))
    else:
        reg_form = AuthorRegisterForm()

    context = dict()
    context['reg_form'] = reg_form
    return render(request, 'account/author_register.html', context)


@login_required
def profile(request):
    context = dict()
    return render(request, 'profile.html', context)


class BookShelfListView(ListView, LoginRequiredMixin):
    model = Bookshelf()
    template_name = 'account/book_shelf.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        self.owner = get_object_or_404(User, pk=self.kwargs['pk'])
        return Bookshelf.objects.filter(owner=self.owner)

