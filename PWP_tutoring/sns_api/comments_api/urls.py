from django.urls import path
from . import views

app_name = 'comments_api'

urlpatterns = [
    path('', views.comment_list, name='comment-list'),
    path('create/', views.comment_create, name='comment-create'),
]