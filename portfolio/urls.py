from django.urls import path
from django.http import HttpResponse
from portfolio import views
urlpatterns = [
    path('', views.base),
]