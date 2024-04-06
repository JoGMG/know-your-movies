#!/usr/bin/python3
""" Genre data model (KYM). """
from models.base_model import BaseModel, Base, os, \
      Column, String, ForeignKey, relationship


class Genre(BaseModel, Base):
    """ Genre class (inherits from BaseModel). """
    __tablename__ = 'genres'
    movie_id = Column(
        String(64), ForeignKey('movies.id'), nullable=False
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    name = Column(
        String(64), nullable=False
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    if os.getenv('KYM_STORAGE') == 'db':
        movies = relationship('Movie', back_populates='genres')
    else:
        @property
        def movies(self):
            """
            Returns the movie instances of this genre instance.
            """
            from models import storage
            from models.movie import Movie
            genre_movies = []
            for movie in storage.all(Movie).values():
                if movie.id == self.movie_id:
                    genre_movies.append(movie.to_dict())
            return genre_movies
