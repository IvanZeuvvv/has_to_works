from django.urls import path
from .views import NewsHomePage, Create, NewsDetail, NewsEdit, Contacts, Account


urlpatterns = [
    path('', NewsHomePage.as_view(), name='news'),
    path('contacts', Contacts.as_view(), name='contacts'),
    path('create', Create.as_view(), name='create'),
    path('<int:pk>', NewsDetail.as_view(), name='detail_news'),
    path('<int:news_id>/edit', NewsEdit.as_view(), name='news_edit'),
    path('account', Account.as_view(), name='account')

]