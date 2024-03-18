
from django.db import models
from django.urls import reverse

class Genre(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def get_absolute_url(self):
        return reverse('filmzoneapp:movies_by_genre', args=[self.slug])

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    description = models.TextField(blank=True)
    release_date = models.DateField()
    cast = models.TextField(blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    ytube_trailer = models.URLField()




    class Meta:
        ordering = ('title',)
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def get_absolute_url(self):
        return reverse('filmzoneapp:movie_detail', args=[self.genre.slug, self.slug])

    def __str__(self):
        return self.title



