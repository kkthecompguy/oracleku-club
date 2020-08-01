from django.urls import path
from .views import index, event_detail

app_name = 'events'
urlpatterns = [
  path('', index, name='index'),
  path('<str:slug>', event_detail, name='events-detail'),
]