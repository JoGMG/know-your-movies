#!/usr/bin/python3
""" Cast data model (KYM). """
from models.base_model import BaseModel, Base, os,\
      Column, String, Integer, ForeignKey, relationship


class Cast(BaseModel, Base):
    """ Cast class (inherits from BaseModel). """
    __tablename__ = 'cast'
    movie_id = Column(
        String(64), ForeignKey('movies.id'), nullable=False
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    original_name = Column(
        String(128), nullable=False
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    character_name = Column(
        String(128), nullable=False
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    gender = Column(
        String(64), nullable=False
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    age = Column(
        Integer, nullable=True
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    headshot_path = Column(
        String(256), nullable=True
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    about = Column(
        String(640), nullable=True
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    if os.getenv('KYM_STORAGE') == 'db':
        movies = relationship(
            'Movie',
            back_populates='cast'
        )
    else:
        @property
        def movies(self):
            """
            Returns the movie instances of this cast instance.
            """
            from models import storage
            from models.movie import Movie
            cast_movies = []
            for movie in storage.all(Movie).values():
                if movie.id == self.movie_id:
                    cast_movies.append(movie.to_dict())
            return cast_movies
