from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('create/', views.CreateView.as_view(), name="create"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
]