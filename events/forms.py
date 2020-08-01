from django import forms
from tinymce import TinyMCE
from .models import Event


class TinyMCEWidget(TinyMCE):
  def use_required_attribute(self, *args):
    return False


class EventForm(forms.ModelForm):
  description = forms.CharField(widget=TinyMCEWidget(attrs={
    'required': False,
    'cols': 30,
    'rows': 10
  }))

  class Meta:
    model = Event
    fields = ['title', 'overview', 'description', 'thumbnail', 'event_date', 'from_time', 'to_time', 'event_type', 'venue', 'featured', ]