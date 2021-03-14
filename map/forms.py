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
        fields = ("title", "text", "date_start", "date_end")

    def save(self, lat, lon, commit=True):
        event = super(NewEventForm, self).save(commit=False)
        event.lat = lat
        event.lon = lon
        if commit:
            event.save()
        return event

class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ("title", "text")

    def save(self, lat, lon, commit=True):
        place = super(NewPlaceForm, self).save(commit=False)
        place.lat = lat
        place.lon = lon
        if commit:
            place.save()
        return place


class PreferencesForm(forms.ModelForm):
   class Meta:
       model = Profile
       fields = ['tags','avatar']
       widgets = {
            'tags': forms.CheckboxSelectMultiple(attrs={'queryset': Tag.objects.all()}),
        }

    #name = forms.CharField(max_length=100)
    #email = forms.EmailField(required=True)
    #avatar = forms.ImageField(height_field=None, width_field=None, max_length=100)
    #skills = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset = Skill.objects.all())
