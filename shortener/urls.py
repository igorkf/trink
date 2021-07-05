from django.urls import path

from . import views

urlpatterns = [
    path('links/', views.LinksView.as_view(), name='links'),
    path('redirect/<path:shortened_url>', views.RedirectView.as_view(), name='redirect'),
    path('shortener/', views.ShortenerView.as_view(), name='shortener')
]
