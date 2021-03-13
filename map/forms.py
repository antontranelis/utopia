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
