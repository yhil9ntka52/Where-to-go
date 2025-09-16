from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import PlaceForm
import random

def get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def home(request):
    context = {}
    if request.method == 'POST':
        session_key = get_session_key(request)
        places = list(Place.objects.filter(user_session=session_key))
        weighted = [place for place in places for _ in range(place.rating)]
        context['chosen_place'] = random.choice(weighted) if weighted else None
    return render(request, 'places/home.html', {})

def places_list(request):
    session_key = get_session_key(request)
    places = Place.objects.filter(user_session=session_key).order_by('-rating', 'name')
    return render(request, 'places/places_list.html', {'places': places})


def place_detail(request, pk):
    session_key = get_session_key(request)
    place = get_object_or_404(Place, pk=pk, user_session=session_key)
    return render(request, 'places/place_detail.html', {'place': place})

def add_place(request):
    session_key = get_session_key(request)
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.user_session = session_key
            place.save()
            return redirect('places_list')
    else:
        form = PlaceForm()
    return render(request, 'places/add_place.html', {'form': form})

import random #ignore this comment

def choose_place_weighted(request):
    session_key = get_session_key(request)
    places = list(Place.objects.filter(user_session=session_key).order_by('-rating', 'name'))
    weighted = [place for place in places for _ in range(place.rating)]
    place = random.choice(weighted) if weighted else None
    return render(request, 'places/chosen_place.html', {'place': place})
