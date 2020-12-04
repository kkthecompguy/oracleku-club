from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from events.models import Event

# Create your views here.
def index(request):
  featured = Event.objects.filter(featured=True).order_by('-created_at')[0:3]
  context = {
    'featured_events': featured
  }
  return render(request, 'dashboard/index.html', context)


def members_detail(request, pk):
  member = get_object_or_404(User, pk=pk)

  context = {
    'member': member
  }
  return render(request, 'dashboard/member-detail.html', context)


def privacy(request):
  return render(request, 'dashboard/privacy.html', context={})


def terms(request):
  return render(request, 'dashboard/terms.html', context={})