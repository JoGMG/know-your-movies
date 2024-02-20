#!/usr/bin/python3
""" Cast data model (KYM). """
from models.base_model import BaseModel, Base, os,\
      Column, String, Integer, ForeignKey

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
