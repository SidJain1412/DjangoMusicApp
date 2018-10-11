from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
# Create your views here.


def index(request):
    html = ''
    all_albums = Album.objects.all()
    for album in all_albums:
        url = 'music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + "</a><br>"
    return HttpResponse("<h1>Hello</h1>")


def detail(request, album_id):
    return HttpResponse("<h2>Details for Album ID: " + str(album_id) + " </h2>")
