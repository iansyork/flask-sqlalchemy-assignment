from src.models import db, Movie

class MovieRepository:

    def get_all_movies(self):
        all_movies = Movie.query.all()
        return all_movies

    def get_movie_by_id(self, movie_id):
        movie_by_id = Movie.query.get(movie_id)
        return movie_by_id

    def create_movie(self, title, director, rating):
        new_movie = Movie(title=title, director=director, rating=rating)
        db.session.add(new_movie)
        db.session.commit()
        return new_movie

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        movie_search = Movie.query.filter(Movie.title.ilike(f'%{title}%')).all()
        return movie_search

# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
