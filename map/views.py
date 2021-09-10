from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Event, Place, Tag, Profile, Offer
from django.contrib.auth.models import User
from .forms import NewUserForm, NewEventForm, NewPlaceForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import serializers
from django.utils.timezone import localtime, now

def map(request,event=0,place=0,people=0):
    if event != 0:
        event = Event.objects.filter(pk=event)
        event = event[0]
    if place != 0:
        place = Place.objects.filter(pk=place)
        place = place[0]
    if people != 0:
        people = User.objects.filter(pk=people)
        people = people[0]
    eventForm = NewEventForm
    placeForm = NewPlaceForm
    eventsJSON = serializers.serialize('json', Event.objects.filter(date_end__gte = localtime(now()).date()))
    placesJSON = serializers.serialize('json', Place.objects.all())
    profilesJSON = serializers.serialize('json', Profile.objects.all())
    tagsJSON = serializers.serialize('json', Tag.objects.all())
    offersJSON = serializers.serialize('json', Offer.objects.all())
    userNameJSON = serializers.serialize('json', User.objects.all(), fields=('username'))
    return render(request=request,
                  template_name="map/map.html",
                  context={"events": eventsJSON, "places": placesJSON, "profiles": profilesJSON, "tags": tagsJSON, "offers": offersJSON, "users": userNameJSON, "event_form":eventForm, "place_form":placeForm, "open_event": event, "open_people":people, "open_place": place})

def api_request(request):
    if request.POST['type'] == "user_position":
        profile = Profile.objects.get(user=request.user)
        profile.lat = float(request.POST['lat'])
        profile.lon = float(request.POST['lng'])
        profile.save()
        return JsonResponse({"success" : True})

    if request.POST['type'] == "delete_event":
        event = Event.objects.get(pk=request.POST['id']).delete()
        return JsonResponse({"success" : True})

    if request.POST['type'] == "delete_place":
        event = Place.objects.get(pk=request.POST['id']).delete()
        return JsonResponse({"success" : True})

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
            place = form.save(lat, lon, creator)
            return JsonResponse({"object" : serializers.serialize('json', Place.objects.filter(pk=place.pk))})
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    if request.POST['type'] == "event":
        if request.POST['event_id'] != "":
            form = NewEventForm(instance=Event.objects.get(id=request.POST['event_id']), data=request.POST)
        else:
            form = NewEventForm(request.POST)
        if form.is_valid():
            lat = request.POST['lat']
            lon = request.POST['lon']
            if request.user.is_authenticated:
                creator = request.user
            else:
                creator = None
            event = form.save(lat, lon, creator)
            return JsonResponse({"object" : serializers.serialize('json', Event.objects.filter(pk=event.pk))})
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

def profile(request, profilename):
    user = request.user
    profile = User.objects.filter(username=profilename)
    return render(request=request,
                  template_name="map/profile.html",
                  context={"user": user, "profile": profile[0], "tagset": Tag.objects.all})

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
                messages.error(request, "password fields did not match or the password is to weak")

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
def settings(request):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(instance=profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            offers = request.POST.getlist('offers')
            requests = request.POST.getlist('requests')
            form.save(offers,requests)
            messages.success(request, f"Preferences updated for {profile.user.username}")
            return redirect("map:map")

    offerset = Offer.objects.all

    user = request.user
    initial_data = {
        "offers": user.profile.offers.all(),
        "avatar": user.profile.avatar,
        "text": user.profile.text,
    }
    form = ProfileForm(initial=initial_data)
    return render(request=request,
                  template_name="map/settings.html",
                  context={"form": form, "offerset" : offerset})
