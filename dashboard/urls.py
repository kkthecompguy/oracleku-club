from django.urls import path
from .views import index, members_detail, privacy, terms

app_name = 'dashboard'
urlpatterns = [
  path('', index, name='index'),
  path('members/<str:pk>', members_detail, name='members-detail'),
  path('privacy-policy', privacy, name='privacy'),
  path('terms-and-conditions', terms, name='terms'),
]