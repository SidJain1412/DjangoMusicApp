from django.shortcuts import render, get_object_or_404
from .models import Album, Song
# from django.template import loader
# Create your views here.


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    # get object or 404 returns 404 if object not found
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        # Using getlist because checkbox gives a list
        ticked_songs = request.POST.getlist('song')
        print(ticked_songs)
        for i in ticked_songs:
            selected_song = album.song_set.get(pk=i)
            print(selected_song.is_favorite)
            if selected_song.is_favorite:
                selected_song.is_favorite = False
            else:
                selected_song.is_favorite = True
            selected_song.save()
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "Select a valid song please"
        })
    # else:
    #     selected_song.is_favorite = True
    #     selected_song.save()
    return render(request, 'music/detail.html', {'album': album})
