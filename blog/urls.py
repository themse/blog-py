from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog-home'),
    path('post/<slug:slug>', views.post, name='blog-post-detail'),
    path('about', views.about, name='blog-about')
]
