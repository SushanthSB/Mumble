from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True #make email field unique
User._meta.get_field('email').blank = False #make email field required
from django import forms
from .models import Album, Song

class UserForm(forms.ModelForm):
	confirm_password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'password'}))

	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'confirm_password']
		widgets = {
			'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'must be unique...'}),
			'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'E-mail'}),
			'password': forms.TextInput(attrs={'class':'form-control','type':'password'}),
		}

class LoginForm(forms.Form):
	username = forms.CharField(label="Username or email", max_length=500, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username or Email...'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class AlbumForm(forms.ModelForm):

	class Meta:
		model = Album
		fields = ['artist', 'album_title', 'genres', 'album_logo']
		widgets = {
			'artist': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Artist...'}),
			'album_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Album name...'}),
			'genres': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Genre...'}),
		}

class SongForm(forms.ModelForm):

	class Meta:
		model = Song
		fields = ['song_title', 'file_type', 'song']
		widgets = {
			'song_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Song name...'}),
			'file_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'mp3, wav...'}),
		}