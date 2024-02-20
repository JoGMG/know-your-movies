#!/usr/bin/python3
""" Movie data model (KYM). """
from models.base_model import BaseModel, Base, os,\
      Column, String, Integer, Date, relationship

class Movie(BaseModel, Base):
    """ Movie class (inherits from BaseModel). """
    __tablename__ = 'movies'
    title = Column(
        String(128), nullable=False
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    release_date = Column(
        Date, nullable=False
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    poster_path = Column(
        String(256), nullable=True
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    overview = Column(
        String(640), nullable=True
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    if os.getenv('KYM_STORAGE') == 'db':
        cast = relationship(
            'Cast',
            cascade='all, delete, delete-orphan',
            backref='movies'
        )
    else:
        @property
        def cast(self):
            """ Returns the cast of a movie instance. """
            from models import storage
            from models.cast import Cast
            movie_cast = []
            for cast in storage.all(Cast).values():
                if cast.movie_id == self.id:
                    movie_cast.append(cast.to_dict())
            return movie_cast
    if os.getenv('KYM_STORAGE') == 'db':
        reviews = relationship(
            'Review',
            cascade='all, delete, delete-orphan',
            backref='movie'
        )
    else:
        @property
        def reviews(self):
            """ Returns the reviews of a movie instance. """
            from models import storage
            from models.review import Review
            movie_reviews = []
            for review in storage.all(Review).values():
                if review.movie_id == self.id:
                    movie_reviews.append(review.to_dict())
            return movie_reviews
