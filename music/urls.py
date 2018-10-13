from django.urls import path
from . import views
# specifying appname for use in templating
app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/23
    path('<int:album_id>/', views.detail, name='detail'),

    # /music/<album_id>/favorite/
    path('<int:album_id>/favorite/', views.favorite, name='favorite')
]
