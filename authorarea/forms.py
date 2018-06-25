from django import forms
from book.models import Book, Category, Volume


class CreateBookForm(forms.Form):
    category = forms.ModelChoiceField(label='分类', queryset=Category.objects.all())
    name = forms.CharField(label='书名', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cover = forms.ImageField(label='封面')
    summary = forms.CharField(label='简介', widget=forms.Textarea(attrs={'class': 'form-control'}))

    def clean_name(self):
        name = self.cleaned_data['name']
        if Book.objects.filter(name=name).exists():
            return forms.ValidationError('书名已存在')
        return name


class AddNewVolumeForm(forms.Form):
    name = forms.CharField(label='卷名', widget=forms.TextInput(attrs={'class': 'form-control'}))


class UpdateBookForm(forms.Form):
    volume_from = forms.ModelChoiceField(label='卷名', queryset=Volume.objects.all())
    name = forms.CharField(label='章节', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='内容', widget=forms.Textarea(attrs={'class': 'form-control',
                                                                       'onkeyup': "inputTest(this.value)"
                                                                        }))


