from django.urls import path
from .views import index, members_detail

app_name = 'dashboard'
urlpatterns = [
  path('', index, name='index'),
  path('members/<str:pk>', members_detail, name='members-detail'),
]