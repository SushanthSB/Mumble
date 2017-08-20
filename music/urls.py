from django.views.generic import TemplateView
from . import views
from django.conf.urls import url

urlpatterns = [
	
	#/
	url(r'^$', views.UserFormView.as_view(), name="index"),
	
	#/music/
	url(r'^music/$',views.IndexView.as_view(), name='home'),

	#/login/
	url(r'^login/$', views.LoginFormView.as_view(), name="login"),
	
	#/logout/
	url(r'^logout/$', views.LogoutView.as_view(), name="logout"),
	
	#/id/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='album_detail'),

	#/id/favorite/
	url(r'^(?P<pk>[0-9]+)/favorite/$', views.AlbumFavorite.as_view(), name='album_favorite'),

	#/album/add/
	url(r'^album/add/$', views.AlbumCreate.as_view(), name='album_create'),

	#/album/2/
	url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name="album_update"),

	#/album/2/delete/
	url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name="album_delete"),

	#/id/songadd/
	url(r'^(?P<pk>[0-9]+)/songadd/$', views.SongAdd.as_view(), name="song_add"),

	#/songs/
	url(r'^album/songs/$', views.SongsList.as_view(), name="songs"),

	#/songs/2/
	url(r'^songs/(?P<pk>[0-9]+)/$', views.SongFavorite.as_view(), name="song_favorite"),

	#/id/song-id/delete/
	url(r'^song/(?P<pk>[0-9]+)/(?P<sid>[0-9]+)/delete/$', views.SongDelete.as_view(), name="song_delete"),

	#/album/2/
	url(r'^song/(?P<pk>[0-9]+)/update/$', views.SongUpdate.as_view(), name="song_update"),
]
