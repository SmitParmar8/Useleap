from django.shortcuts import render
from .models import movie
# Create your views here.
def home(request):
    searchMovie = request.GET.get("searchMovie")
    if searchMovie :
        movies = movie.objects.filter(title__icontains=searchMovie)
    else :
        movies = movie.objects.all()
    return render(request,'home.html',{'searchTerm' : searchMovie , "movies" :movies})