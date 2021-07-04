from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('links/', views.LinksView.as_view()),
    path('shortener/', views.ShortenerView.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
