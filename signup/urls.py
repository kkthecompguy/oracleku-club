from django.urls import path
from .views import index, signin

app_name = 'signup'
urlpatterns = [
  path('signup', index, name='index'),
  path('signin', signin, name='login'),
]