"""
Django settings for RechteDB project.

Generated by 'django-admin startproject' using Django 1.11.14.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'itc%syf=c5pv0wtk1rp=1%+ngib3t(6lu&tp3-1!qv_1rs384+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
INTERNAL_IPS = ('127.0.0.1','192.168.21.36','192.168.21.29','192.168.21.30')

# Application definition

INSTALLED_APPS = [
	'rapp',
	'django_filters',
	'django.contrib.admindocs',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'widget_tweaks',
	'debug_toolbar',
	'bootstrap4',
	'import_export',
]

MIDDLEWARE = [
	'debug_toolbar.middleware.DebugToolbarMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'RechteDB.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': ['./templates', ],
		# 'DIRS': [os.path.join(BASE_DIR, 'templates')],		# Todo Pfade richtig setzen und Files verteilen!!!
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'django.template.context_processors.request',
			],
		},
	},
]

WSGI_APPLICATION = 'RechteDB.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
	'default': {	# Konfiguration gegen Mainfrix-Container
		'ENGINE': 'django.db.backends.mysql',  # ToDo Remote MySQL DB anbinden / Config anpassen über meinNetz
		'NAME': 'RechteDB',
		'USER': 'RechteFuzzi',
		'PASSWORD': 'Nn9ryRCh3342554323455235254235z2m7zEbwTvM',
		'HOST': '192.168.21.36',
		'PORT': '13306',
		'default-character-set': 'utf8mb4_unicode_ci',
		'OPTIONS': {
			'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
		}
	},

	# Alte Standardkonfiguration gegen Naschef mysql ohne Container
	'naschef-Server-reichlich-kaputt': {
		# 'ENGINE': 'django.db.backends.sqlite3',
		# 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		'ENGINE': 'django.db.backends.mysql',		# ToDo Remote MySQL DB anbinden / Config anpassen über meinNetz
		# 'read_default_file': os.path.join(BASE_DIR, 'my.cnf'),
		'NAME': 'RechteDB',
		'USER': 'RechteFuzzi',
		'PASSWORD': 'Nn9ryRCh3342554323455235254235z2m7zEbwTvM',
		'HOST': '192.168.21.29',
		'PORT': '3306',
		'default-character-set': 'utf8mb4_unicode_ci',
		'OPTIONS': {
			'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
		}
	}
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'de-DE'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
IMPORT_EXPORT_USE_TRANSACTIONS = True
