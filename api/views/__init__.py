#!/usr/bin/python3
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api')

from api.views.index import *
from api.views.users import *
from api.views.movie_reviews import *
from api.views.movies import *
from api.views.cast import *
from api.views.reviews import *
from api.views.genre import *
