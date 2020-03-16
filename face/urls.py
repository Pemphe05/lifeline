from django.urls import path
from .views import homePageView, newPageView, nextPageView


app_name='face'
urlpatterns = [
path('', homePageView, name='home'),
path('new/', newPageView, name='new'),
path('next/', nextPageView, name='next'),
]