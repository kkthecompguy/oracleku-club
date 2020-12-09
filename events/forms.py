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
  title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  slug = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  overview = forms.Textarea(attrs={'class': 'form-control'})
  event_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
  from_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
  to_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
  venue = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  event_link = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

  class Meta:
    model = Event
    fields = ['title','slug', 'overview', 'description', 'thumbnail', 'event_date', 'from_time', 'to_time', 'event_type', 'venue', 'featured', 'event_link']
  
  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    self.fields['venue', 'event_link'].required = False