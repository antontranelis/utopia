from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event, Place, Tag, Profile
from .forms import NewUserForm, NewEventForm, NewPlaceForm, PreferencesForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import serializers
import datetime
# Create your views here.

def map(request):
    if request.method == "POST":
        if request.POST['type'] == "user_position":
            profile = Profile.objects.get(user=request.user)
            profile.lat = float(request.POST['lat'])
            profile.lon = float(request.POST['lng'])
            profile.save()
            messages.success(request, f"You added your position to the map")
            return redirect("map:map")
        if request.POST['type'] == "event":
            if request.POST['event_id'] != "":
                form = NewEventForm(instance=Event.objects.get(id=request.POST['event_id']), data=request.POST)
            else:
                form = NewEventForm(request.POST)
        if request.POST['type'] == "place":
            if request.POST['place_id'] != "":
                form = NewPlaceForm(instance=Place.objects.get(id=request.POST['place_id']), data=request.POST)
            else:
                form = NewPlaceForm(request.POST)
        if form.is_valid():
            lat = request.POST['lat']
            lon = request.POST['lon']
            if request.user.is_authenticated:
                creator = request.user
            else:
                creator = None
            form.save(lat, lon, creator)
            if request.POST['type'] == "event":
                if request.POST['event_id'] != "":
                    messages.success(request, f"Event updated")
                else:
                    messages.success(request, f"New event created")
            if request.POST['type'] == "place":
                if request.POST['place_id'] != "":
                    messages.success(request, f"Place updated")
                else:
                    messages.success(request, f"New place created")
            return redirect("map:map")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")


    eventForm = NewEventForm
    placeForm = NewPlaceForm
    eventsJSON = serializers.serialize('json', Event.objects.filter(date_end__gte = datetime.date.today()))
    placesJSON = serializers.serialize('json', Place.objects.all())
    tagsJSON = serializers.serialize('json', Tag.objects.all())
    return render(request=request,
                  template_name="map/map.html",
                  context={"events": eventsJSON, "places": placesJSON, "user_profiles": Profile.objects.all(), "tags": tagsJSON, "event_form":eventForm, "place_form":placeForm})

def profile(request):
    user = request.user
    return render(request=request,
                  template_name="map/profile.html",
                  context={"user": user, "tagset": Tag.objects.all})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            profile = Profile(user=user)
            profile.save()
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("map:map")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request,
                  "map/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("map:map")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')

    form = AuthenticationForm()
    return render(request, "map/login.html", context={"form":form})

@login_required
def preferences(request):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        form = PreferencesForm(instance=profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Preferences updated for {profile.user.username}")
            return redirect("map:map")



    user = request.user
    initial_data = {
        "tags": user.profile.tags.all(),
        "avatar": user.profile.avatar,
    }
    form = PreferencesForm(initial=initial_data)
    return render(request=request,
                  template_name="map/preferences.html",
                  context={"form": form})
