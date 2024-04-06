#!/usr/bin/python3
""" User data model (KYM). """
from models.base_model import BaseModel, Base, os, \
      Column, String, relationship


class User(BaseModel, Base):
    """ User class (inherits from BaseModel). """
    __tablename__ = 'users'
    email = Column(
        String(128), nullable=False
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    name = Column(
        String(128), nullable=True
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            'Review',
            back_populates='user'
        )
    else:
        @property
        def reviews(self):
            """
            Returns the review instances of this user instance.
            """
            from models import storage
            from models.review import Review
            user_reviews = []
            for review in storage.all(Review).values():
                if review.user_id == self.id:
                    user_reviews.append(review.to_dict())
            return user_reviews
