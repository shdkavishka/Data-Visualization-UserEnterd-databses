import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Function to fetch database credentials from environment variables
def get_user_database_credentials():
    return {
        'ENGINE': os.environ.get('USER_DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('USER_DB_NAME', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('USER_DB_USER', ''),
        'PASSWORD': os.environ.get('USER_DB_PASSWORD', ''),
        'HOST': os.environ.get('USER_DB_HOST', ''),
        'PORT': os.environ.get('USER_DB_PORT', ''),
    }

# Fetch user-defined database credentials dynamically
USER_DATABASES = {
    'default': get_user_database_credentials()
}

# PostgreSQL database configuration
DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'postgresql': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRESQL_DB_NAME', ''),
        'USER': os.environ.get('POSTGRESQL_DB_USER', ''),
        'PASSWORD': os.environ.get('POSTGRESQL_DB_PASSWORD', ''),
        'HOST': os.environ.get('POSTGRESQL_DB_HOST', ''),
        'PORT': os.environ.get('POSTGRESQL_DB_PORT', '5432'),  # Default port for PostgreSQL
    },
}


  
