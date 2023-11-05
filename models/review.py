#!/usr/bin/python3
""" Review data model (KYM). """
from models.base_model import BaseModel, Base, os, datetime,\
    Column, String, ForeignKey, DATETIME

class Review(BaseModel, Base):
    """ Review class (inherits from BaseModel). """
    __tablename__ = 'reviews'
    movie_id = Column(
        String(64), ForeignKey('movies.id'), nullable=False
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    user_id = Column(
        String(64), ForeignKey('users.id'), nullable=False
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    date = Column(
        DATETIME, nullable=False, default=datetime.utcnow()
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
    text = Column(
        String(1024), nullable=False
    ) if os.getenv('KYM_STORAGE') == 'db' else ''
