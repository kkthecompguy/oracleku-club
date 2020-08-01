from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Event, Attendee


# Create your views here.
def index(request):
  events = Event.objects.all()
  context = {
    'events': events
  }
  return render(request, 'events/index.html', context)


def event_detail(request, slug):
  event = get_object_or_404(Event, slug=slug)
  user_already_in_list = None
  event_list = []
  if request.user.is_authenticated:
    for user in event.attendees.all():
      event_list.append(user.email)
    if request.user.email in event_list:
      user_already_in_list = request.user.email

  if request.method == 'POST':
    if request.user.is_authenticated:
      user = request.user
      if user_already_in_list:
        messages.error(request, 'You are already attending', fail_silently=True)
        return render(request, 'events/event-detail.html', {'event': event, 'user_already_in_list': user_already_in_list})
      else:
        event.attendees.create(user=user, email=user.email, first_name=user.first_name, last_name=user.last_name)
        return redirect('events:events-detail', slug=slug)
    else:
      return redirect(f'/users/signin?next=/events/{slug}')

  context = {
    'event': event,
    'user_already_in_list': user_already_in_list
  }
  return render(request, 'events/event-detail.html', context)