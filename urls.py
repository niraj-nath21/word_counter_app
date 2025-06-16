from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter/', views.counter, name='counter'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('post/<str:pk>/', views.post, name='post'),  # Dynamic URL routing: <str:pk> captures a string parameter from the URL and passes it to the post view as the pk argument.
]