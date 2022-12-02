from django import forms
from django.shortcuts import render, redirect
from django.views import View, generic
from .models import Articles, Comments
from .forms import ArticlesForm, CommentsForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView

class NewsHomePage(ListView):
    model = Articles
    template_name = "add_news/news_home.html"
    context_object_name = "news"
    extra_context = {'title': 'Главная'}


class Contacts(TemplateView):
    template_name = "add_news/contacts.html"


class Create(CreateView):
    form_class = ArticlesForm
    template_name = 'add_news/create.html'



class NewsDetail(generic.DetailView):
    model = Articles
    template_name = 'add_news/detail_news.html'
    context_object_name = 'detail_news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_id'] = self.object.id
        context['comments_list'] = Comments.objects.filter(news_id=self.object.id)
        context['comment_form'] = CommentsForm()
        return context

    def post(self, request, **kwargs):
        detail_news = self.get_object()
        comments_form = CommentsForm(request.POST)
        if comments_form.is_valid():
            Comments.objects.create(news=detail_news, **comments_form.cleaned_data)
            return HttpResponseRedirect(f'{detail_news.id}')
        return render(request, 'add_news/detail_news.html', context={'comments_form': comments_form,
                                                                     'detail_news': detail_news})


class NewsEdit(UpdateView):
    model = Articles
    fields = ['title', 'anons', 'text_news', 'date_add', 'update_date']
    template_name_suffix = 'add_news/edit.html'

    #def get(self, request, news_id):
        #news = Articles.objects.get(id=news_id)
        #news_form = ArticlesForm(instance=news)
        #return render(request, 'add_news/edit.html', context={'news_form': news_form, 'news_id': news_id})

    #def post(self, request, news_id):
        #news = Articles.objects.get(id=news_id)
        #news_form = ArticlesForm(request.POST, instance=news)
        #if news_form.is_valid():
            #news_form.save()
            #return redirect('news')
        #return render(request, 'add_news/edit.html', context={'news_form': news_form, 'news_id': news_id})
#

class CommentsBlock(ListView):
    model = Comments
    template_name = "add_news/detail_news.html"
    context_object_name = "news"

class Account(TemplateView):
    template_name = "add_news/account.html"
# def get(self, request):


      #  comments = Comments.objects.all()


       # return render(request, 'add_news/detail_news.html', context={'comments': comments})


class ArticlesDetail(DetailView):
    model = Articles
    template_name = 'add_news/detail_news.html'
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = Comments.objects.filter(news_id=self.object.id)
        comment_form = CommentsForm()
        if self.request.user.is_authenticated:
            comment_form.fields['name'].widget = forms.HiddenInput()
            context['comment_form'] = comment_form
        else:
            context['comment_form'] = CommentsForm()

        return context

    def post(self, request, **kwargs):
        detail = self.get_object()
        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.news = self.get_object()
            if self.request.user.is_authenticated:
                comment.name = self.request.user.username
            else:
                comment.name = comment_form.cleaned_data.get('name') + ' / Аноним'
            comment.save()
            return redirect('index')
        return render(request, 'add_news/detail_news.html',
                      context={'comment_form': comment_form, 'detail': detail})