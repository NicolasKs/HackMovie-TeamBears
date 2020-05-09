from gateway.show_movies import get_movies
from models.movie import Movie
from views.templates.show_movies import display_movies


def show_movies_command():
    movies_raw_data = get_movies()
    movies = map_movies(movies_raw_data)
    display_movies(movies)


def map_movies(movies_raw_data):
    return list(map(lambda props: Movie.create_model(props), movies_raw_data))