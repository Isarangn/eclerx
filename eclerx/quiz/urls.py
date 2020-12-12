from django.urls import path
from quiz import views


urlpatterns = [
    path('', views.exam, name='home'),
]
