from django.urls import path

from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('create/', views.CreateView.as_view(), name="create"),
]