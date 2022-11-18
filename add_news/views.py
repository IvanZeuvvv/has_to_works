from django.shortcuts import render, redirect
from django.views import View, generic
from .models import Articles, Comments
from .forms import ArticlesForm, CommentsForm
from django.http import HttpResponseRedirect


class NewsHomePage(View):

    def get(self, request):
        news = Articles.objects.order_by('-date_add')
        return render(request, 'add_news/news_home.html', {'news': news})


class Contacts(View):
    def get(self, request):
        return render(request, 'add_news/contacts.html', {})


class Create(View):

    def get(self, request):

        news_form = ArticlesForm()

        return render(request, 'add_news/create.html', context={'news_form': news_form})

    def post(self, request):
        news_form = ArticlesForm(request.POST)
        if news_form.is_valid():
            news_form.save()
            return redirect('news')
        else:
            errors = 'Вы неверно заполнили форму'
        return render(request, 'add_news/create.html', context={'news_form': news_form, 'errors': errors})


class NewsDetail(generic.DetailView):
    model = Articles
    template_name = 'add_news/detail_news.html'
    context_object_name = 'detail_news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_id'] = self.object.id
        context['comments_list'] = Comments.objects.filter(news_id=self.object.id).all()
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


class NewsEdit(View):

    def get(self, request, news_id):
        news = Articles.objects.get(id=news_id)
        news_form = ArticlesForm(instance=news)
        return render(request, 'add_news/edit.html', context={'news_form': news_form, 'news_id': news_id})

    def post(self, request, news_id):
        news = Articles.objects.get(id=news_id)
        news_form = ArticlesForm(request.POST, instance=news)
        if news_form.is_valid():
            news_form.save()
            return redirect('news')
        return render(request, 'add_news/edit.html', context={'news_form': news_form, 'news_id': news_id})


class CommentsBlock(View):
    def get(self, request):
        comments = Comments.objects.all()
        return render(request, 'add_news/detail_news.html', context={'comments': comments})