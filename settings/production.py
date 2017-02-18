import ast
import os

from .base import *  # NOQA


DEBUG = ast.literal_eval(os.environ.get('DEBUG', 'False'))
SECRET_KEY = os.environ.get('SECRET_KEY', None)

ALLOWED_HOSTS = ['.herokuapp.com', '0.0.0.0']
