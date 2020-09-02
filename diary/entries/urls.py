from django.urls import path
from . import views

app_name = 'entries'
urlpatterns = [
    path('', views.index, name='index'),
    path('save_entry', views.save, name='save'),
]
