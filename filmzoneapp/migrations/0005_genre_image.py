# Generated by Django 5.0.1 on 2024-02-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmzoneapp', '0004_genre_movie_delete_movies'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='image',
            field=models.ImageField(blank=True, upload_to='genre'),
        ),
    ]