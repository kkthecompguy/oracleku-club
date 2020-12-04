from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Event, Attendee, Subscribe
from .forms import EventForm
from .emails import send_mail


html = """
<!Doctype html>
<html>
<head>
<title>Kenyatta University Oracle Club</title>
</head>
<body>
<p>Hello friend, you are part of the Kenyatta University Oracle Club. A new event has been uploaded. To Find out when and where click <a href="https://oracleku-club.herokuapp.com/events/{}" target="_blank">here</a></p>
<p>See you at the event!!</p>
<a href="https://oracleku-club.herokuapp.com" target="_blank">View Site</a>
</body>
</html>
"""

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


def create_event_view(request):
  form = EventForm(request.POST or None, request.FILES or None)
  if request.method == 'POST':
    if form.is_valid():
      event = form.save(commit=False) 
      event.host = request.user
      event.save()
      subscribers = Subscribe.objects.all()
      email_list = []
      for subscriber in subscribers:
        email_list.append(subscriber.email) 
      for email in email_list:
        sent = send_mail(to_emails=[email], html=html.format(event.slug), subject=event.title)
      return redirect('events:events-detail', slug=event.slug)
  context = {
    'form': form
  }
  return render(request, 'events/create-event.html', context)


def subscribe(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    email_list = []
    subscribers = Subscribe.objects.all() 
    for subscriber in subscribers: 
      email_list.append(subscriber.email)
    if email in email_list:
      messages.error(request, 'You are already subscribed')
    else: 
      sent = send_mail(to_emails=[email])
      if sent:
        Subscribe.objects.create(email=email)
        messages.success(request, 'Thank you for subscribing') 
      else:
        messages.error(request, 'something went wrong. Try again later') 
  return redirect('dashboard:index')