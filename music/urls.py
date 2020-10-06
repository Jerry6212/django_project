from django.urls import path

from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name="index"),


    # /music/#/
    path('<pk>/', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name="album-add"),

    # /music/album/pk/
    path('pk', views.AlbumUpdate.as_view(), name="album-update"),

    # /music/album/pk/delete/
    path('pk+delete', views.AlbumDelete.as_view(), name="album-delete")

]
