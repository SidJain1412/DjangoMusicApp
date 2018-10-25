from django.urls import path
from . import views
# specifying appname for use in templating
app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),

    # /music/23
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /music/<album_id>/favorite/
    # path('<int:album_id>/favorite/', views.favorite, name='favorite')
    # /music/album/add
    path('album/add/', views.CreateView.as_view(), name='alubm-add')
]
