from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('new_post/', views.post_new, name='post_new'),
    path('post/<slug:post_slug>/edit/', views.post_edit, name='post_edit'),
]
