from django.urls import path, include
from .import views

urlpatterns = [
    path("movies/", views.creat_movies, name="movies" ),
    path("movies/<int:id>/", views.get_movies, name="movie"),
    path("ratings/", views.create_ratings, name="rating"),
]
