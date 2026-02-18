import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# Charger les variables du fichier .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# --- SÉCURITÉ ---
# On utilise une clé par défaut seulement pour le local
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-zbl_*whs+^+jg+5@*zzs#m497iz+qn=v6z+9#&i66llbi1%94$')

# DEBUG est True en local, et on le mettra à False en ligne via le .env
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# Autorise localhost et ton futur nom de domaine
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# --- APPS ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # Ajout pour les fichiers statiques
    'django.contrib.staticfiles',
    'eglise', 
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Indispensable pour la prod
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Dossier templates à la racine
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'

# --- BASE DE DONNÉES ---
# Utilise SQLite en local, et PostgreSQL (ou autre) si DATABASE_URL est présent
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}

# --- FICHIERS STATIQUES & MEDIA ---
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' # Pour la prod
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- REDIRECTIONS ---
LOGIN_REDIRECT_URL = '/panel/' 
LOGIN_URL = '/login/' # Ajusté car '//' n'est pas une route valide
LOGOUT_REDIRECT_URL = '/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# # À ajouter tout en bas de settings.py
# CSRF_TRUSTED_ORIGINS = [
#     "https://*.herokuapp.com", 
#     "https://*.render.com",
#     "https://ton-domaine.com" # Si tu as un nom de domaine à toi
# ]

# Configuration pour Render (domaine gratuit)
CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]