from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('KensakuKunn', views.kensaku_kunn, name='KensakuKunn'),
    path('kekka/<int:blog_id>/', views.kekka, name='kekka'),
]
