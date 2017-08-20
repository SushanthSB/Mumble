from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Album, Song
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, LoginForm, AlbumForm, SongForm
from django.http import JsonResponse, HttpResponseRedirect

class IndexView(generic.ListView):
	template_name="music/home.html"
	context_object_name = "albums"

	def get_queryset(self):
		return Album.objects.filter(created_by=self.request.user)

class DetailView(generic.DetailView):
	model = Album
	context_object_name = "albums"
	template_name = 'music/detail.html'

class AlbumCreate(CreateView):
	form_class = AlbumForm
	template_name = "music/album_form.html"

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super(AlbumCreate, self).form_valid(form)

class AlbumUpdate(UpdateView):
	form_class = AlbumForm

	def get_object(self):
		return Album.objects.get(id=self.kwargs['pk'])
	
class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('home')

class SongAdd(CreateView):
	form_class = SongForm
	template_name = 'music/song_form.html'

	def form_valid(self, form):
		album=Album.objects.get(pk=self.kwargs['pk'])
		form.instance.album = album
		return super(SongAdd, self).form_valid(form)

class SongsList(generic.ListView):
	model = Song
	context_object_name = "songs"

	def get_queryset(self):
		album_name=Album.objects.filter(created_by=self.request.user)
		return Song.objects.filter(album=album_name)

class UserFormView(generic.View):
	form_class = UserForm
	template_name = 'music/index.html'

	def get(self, request):
		form = self.form_class(None)
		if request.user.is_authenticated:
			return redirect("home")
		else:
			return render(request, self.template_name, {"form":form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
				form.add_error("confirm_password", "Should be same as password above")
			else:
				user.set_password(form.cleaned_data['password']) #use set_password instead of save() to save password
				user.save()
				form.add_error(None, "Registeration successful !!!")
			return render(request, self.template_name, {'form':form})
		# 	user = form.save(commit=False)

		# 	username = form.cleaned_data['username']
		# 	password = form.cleaned_data['password'] #user.set_password() to change password
		# 	user.set_password(password)
		# 	user.save()

		# 	user = authenticate(username=username, password=password)

		# 	if user is not None:
		# 		if user.is_active:
		# 			login(request, user)
		# 			return redirect("home")

		# return render(request, self.template_name, {'form': form})

class LoginFormView(generic.View):
	
	def get(self, request):
		form = LoginForm(None)
		return render(request, 'music/login.html', {'form':form})

	def post(self, request):
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None:
				login(request, user)
				return redirect("home")
			else:
				form.add_error(None, "Username or password is wrong !!!")
		return render(request, 'music/login.html', {'form':form})

class LogoutView(generic.View):

	def get(self, request):
		logout(request)
		return redirect("index")

class AlbumFavorite(generic.View):

	def get(self, request, pk):
		fav = Album.objects.get(id=pk).is_favorite
		if fav:
			Album.objects.filter(id=pk).update(is_favorite=False)
		else:
			Album.objects.filter(id=pk).update(is_favorite=True)
		return JsonResponse({"status":"200"})

class SongFavorite(generic.View):

	def get(self, request, pk):
		fav = Song.objects.get(id=pk).is_favorite
		if fav:
			Song.objects.filter(id=pk).update(is_favorite=False)
		else:
			Song.objects.filter(id=pk).update(is_favorite=True)
		return JsonResponse({"status":"200"})

class SongDelete(generic.View):
	
	def get(self, request, pk, sid):
		Song.objects.filter(id=sid).delete()
		return HttpResponseRedirect(reverse("album_detail", args=(pk)))

class SongUpdate(UpdateView):
	form_class = SongForm

	def get_object(self):
		return Song.objects.get(id = self.kwargs['pk'])