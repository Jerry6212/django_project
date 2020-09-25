from django.conf.urls import include, url
from django.contrib import admin
from  django.http import Http404
from django.http import HttpResponse
from .models import Album
from django.shortcuts import render

def index(request):
    all_albums = Album.objects.all()
    context = {
        "all_albums": all_albums}
    return render(request, "music/index.html", context)


def detail(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album not found")
    return render(request, "music/index.html", context)
