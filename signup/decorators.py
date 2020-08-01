from django.shortcuts import redirect

def is_authenticated(view_func):
  def wrapper_func(request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect('dashboard:index')
    return view_func(request, *args, **kwargs)
  return wrapper_func