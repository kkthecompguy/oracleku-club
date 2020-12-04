from django.urls import path
from .views import index, event_detail, subscribe, create_event_view

app_name = 'events'
urlpatterns = [
  path('', index, name='index'),
  path('<str:slug>', event_detail, name='events-detail'),
  path('subscribe/', subscribe, name='subscribe'),
  path('create-event/', create_event_view, name='create-event'),
]