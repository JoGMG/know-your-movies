#!/usr/bin/python3
""" Review data model (KYM). """
from models.base_model import BaseModel, Base, os, datetime,\
    Column, String, ForeignKey, relationship


class Review(BaseModel, Base):
    """ Review class (inherits from BaseModel). """
    __tablename__ = 'reviews'
    movie_id = Column(
        String(64), ForeignKey('movies.id'), nullable=False
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    user_id = Column(
        String(64), ForeignKey('users.id'), nullable=False
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    text = Column(
        String(1024), nullable=False
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    if os.getenv('KYM_STORAGE') == 'db':
        movie = relationship(
            'Movie',
            back_populates='reviews'
        )
    else:
        @property
        def movie(self):
            """
            Returns the movie instance of this review instance.
            """
            from models import storage
            from models.movie import Movie
            for movie in storage.all(Movie).values():
                if movie.id == self.movie_id:
                    return movie.to_dict()
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        user = relationship(
            'User',
            back_populates='reviews'
        )
    else:
        @property
        def user(self):
            """
            Returns the user instance of this review instance.
            """
            from models import storage
            from models.user import User
            for user in storage.all(User).values():
                if user.id == self.user_id:
                    return user.to_dict()
