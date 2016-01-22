import os
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )

"""
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join( BASE_DIR, 'sebastian.db' ),
	}
}
"""

DATABASES = {
	'default': {
		'NAME': 'test_1',
		'ENGINE': 'django.db.backends.mysql',
		'USER': 'dem4ply',
		'PASSWORD': 'dem',
		'OPTIONS': {
			'autocommit': True,
		},
	}
}
