from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, Select
from .models import Articles, Comments


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'text_news', 'date_add', 'update_date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'create__input',
            }),
            'anons': TextInput(attrs={
                'class': 'create__input',
            }),
            'text_news': Textarea(attrs={
                'class': 'create__text',
            }),
            'date_add': DateTimeInput(attrs={
                 'class': 'create__input',
             }),
            'update_date': DateTimeInput(attrs={
                 'class': 'create__input',
             })
        }


class CommentsForm(ModelForm):
    username = forms.CharField(max_length=100)

    class Meta:
        model = Comments
        fields = ['text_comment']



        widgets = {
             'username': TextInput(attrs={
                 'class': 'comments__user',
             }),
             'text_comment': Textarea(attrs={
                 'class': 'comments__text',
             })
         }
