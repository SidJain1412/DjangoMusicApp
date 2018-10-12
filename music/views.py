from django.shortcuts import render
from .models import Album
from django.http import Http404
# from django.template import loader
# Create your views here.


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    try:
        album_id = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("That album does not exist")
    return render(request, 'music/detail.html', {'album_id': album_id})
