from django.urls import path
from . import views

app_name = 'polls'  # This is the application namespace

urlpatterns = [
    path('', views.index, name='index'),
    # Add more paths for other views if necessary
]