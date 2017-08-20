from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.

class Album(models.Model):
	artist = models.CharField(max_length=100)
	album_title = models.CharField(max_length=300)
	genres = models.CharField(max_length=100)
	album_logo = models.FileField(upload_to="album_logo/", null=True)
	is_favorite = models.BooleanField(default=False)
	created_on = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('album_detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.album_title +'-'+ self.artist

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type = models.CharField(max_length=10)
	song_title = models.CharField(max_length=100)
	is_favorite = models.BooleanField(default=False)
	song = models.FileField(upload_to="music/", null=True)
	created_on = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse('songs')

	def __str__(self):
		return self.song_title


@receiver(pre_delete, sender=Album)
def Album_delete(sender, instance, **kwargs):
	instance.album_logo.delete(False)

@receiver(pre_delete, sender=Song)
def Song_delete(sender, instance, **kwargs):
	instance.song.delete(False)