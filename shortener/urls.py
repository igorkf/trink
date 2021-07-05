from django.urls import path

from . import views

urlpatterns = [
    path('links/', views.LinksView.as_view(), name='links'),
    path('shortener/', views.ShortenerView.as_view())
]
