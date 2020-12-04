from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from tinymce import HTMLField


class Attendee(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  email = models.EmailField()
  first_name = models.CharField(max_length=100, blank=True)
  last_name = models.CharField(max_length=100, blank=True)

  def __str__(self):
    return self.email

  def get_absolute_url(self):
    return reverse('dashboard:members-detail', kwargs={'pk':self.user.pk})


class Event(models.Model):
  class EventType(models.TextChoices):
    Online_Event = 'Online Event'
    Physical_Event = 'Physical Event'


  slug = models.SlugField(unique=True, max_length=255)
  title = models.CharField(max_length=100)
  overview = models.TextField(max_length=100)
  description = HTMLField()
  host = models.ForeignKey(User, on_delete=models.CASCADE)
  attendees = models.ManyToManyField(Attendee, blank=True, related_name='attendees')
  thumbnail = models.ImageField(upload_to='images/%Y/%m/%d/')
  event_date = models.DateField()
  from_time = models.TimeField()
  to_time = models.TimeField()
  event_type = models.CharField(max_length=50, choices=EventType.choices, default=EventType.Online_Event)
  venue = models.CharField(max_length=100, blank=True, null=True)
  status = models.BooleanField(default=True)
  featured = models.BooleanField(default=False)
  review = models.CharField(max_length=255, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.slug


class Subscribe(models.Model):
  email = models.EmailField()

  def __str__(self):
    return self.email