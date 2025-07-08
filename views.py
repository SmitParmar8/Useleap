from django.shortcuts import render
from .models import Movie
# Create your views here.
def Home(request):
    searchTerm = request.GET.get('searchMovie')
    movies = Movie.objects.all()
    return render(request,'Home.html',{'searchTerm':searchTerm,'movies':movies})
