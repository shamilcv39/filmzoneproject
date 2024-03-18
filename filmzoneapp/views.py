from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import MovieForm
from .models import Movie, Genre


# Create your views here.
def index(request):
    movie = Movie.objects.all()

    context = {
        'movie_list': movie

    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie': movie})

def add_movie(request):
    if request.method == "POST":
        title = request.POST.get('title')
        poster = request.FILES['poster']
        description = request.POST.get('description')
        release_date = request.POST.get('release_date')
        cast = request.POST.get('cast')
        genre_id = request.POST.get('genre')


        genre = Genre.objects.get(id=genre_id)


        new_movie = Movie.objects.create(
            title=title,
            poster=poster,
            description=description,
            release_date=release_date,
            cast=cast,
            genre=genre,
        )

        ytube_trailer = request.POST.get('ytube_trailer')
        new_movie.ytube_trailer = ytube_trailer  # Set ytube_trailer separately
        new_movie.save()

        return redirect('/')


    else:
        genres = Genre.objects.all()
        print(genres)


    return render(request, 'add.html', {'genres': genres})

def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == "POST":
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')


def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})

def movies_by_genre(request, genre_slug):
    genre = get_object_or_404(Genre, slug=genre_slug)
    movies = Movie.objects.filter(genre=genre)
    return render(request, 'movies_by_genre.html', {'genre': genre, 'movies': movies})

def movie_detail(request, genre_slug, movie_slug):
    genre = get_object_or_404(Genre, slug=genre_slug)
    movie = get_object_or_404(Movie, slug=movie_slug, genre=genre)
    return render(request, 'movie_detail.html', {'genre': genre, 'movie': movie})

def search_results(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = []
    return render(request, 'search_results.html', {'movies': movies, 'query': query})

