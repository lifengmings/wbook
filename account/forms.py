from django import forms
from django.contrib import auth
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名或邮箱'}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(
                                attrs={'class': 'form-control', 'placeholder': '请输入密码'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码错误')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名'}))
    email = forms.EmailField(label='邮箱',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱'}))
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}))
    password2 = forms.CharField(label='确认密码',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请确认密码'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('该用户名已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('该邮箱已存在')
        return email

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('两次密码输入不一致')
        return password2


class AuthorRegisterForm(forms.Form):
    pen_name = forms.CharField(label='笔名',
                               max_length=20,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '最大长度为10个汉字或者20字母'}))

    def clean_pen_name(self):
        pen_name = self.cleaned_data['pen_name']
        if User.objects.filter(author__pen_name=pen_name).exists():
            raise forms.ValidationError('该笔名已存在')
        return pen_name
