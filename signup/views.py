from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from .decorators import is_authenticated


# Create your views here.
@is_authenticated
def index(request):
  form = SignUpForm()

  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      # @todo
      # send mail to user
      return redirect('signup:login')
  context = {
    'form': form
  }
  return render(request, 'signup/index.html', context)


@is_authenticated
def signin(request):
  next = request.GET.get('next')

  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      if next:
        return redirect(next)
      else:
        return redirect('/')
  context = {
    'next': next
  }
  return render(request, 'signup/login.html', context)