from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Event, Place, Tag, Profile


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("title", "text", "date_start", "date_end", "tags")
        widgets = {
             'text': forms.Textarea(attrs={'class': 'materialize-textarea'}),
             'tags': forms.CheckboxSelectMultiple(attrs={'queryset': Tag.objects.all(), 'class': 'reset-checkbox'}),
             'date_start': forms.DateInput(attrs={'class': 'datepicker'}),
             'date_end': forms.DateInput(attrs={'class': 'datepicker'}),
         }

    def save(self, lat, lon, creator, commit=True):
        event = super(NewEventForm, self).save(commit=False)
        event.lat = lat
        event.lon = lon
        event.creator = creator
        event.save()
        for tag in self.cleaned_data['tags']:
            event.tags.add(tag)
        if commit:
            event.save()
        return event

class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ("title", "text", "tags")
        widgets = {
             'text': forms.Textarea(attrs={'class': 'materialize-textarea'}),
             'tags': forms.CheckboxSelectMultiple(attrs={'queryset': Tag.objects.all(), 'class': 'reset-checkbox'}),
         }

    def save(self, lat, lon, creator, commit=True):
        place = super(NewPlaceForm, self).save(commit=False)
        place.lat = lat
        place.lon = lon
        place.creator = creator
        place.save()
        for tag in self.cleaned_data['tags']:
            place.tags.add(tag)
        if commit:
            place.save()
        return place


class PreferencesForm(forms.ModelForm):
   class Meta:
       model = Profile
       fields = ['tags', 'avatar']
       widgets = {
             'tags': forms.CheckboxSelectMultiple(attrs={'queryset': Tag.objects.all(), 'class': 'reset-checkbox'}),
        }
