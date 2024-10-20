# eeazycrm/config.py

# Import all configuration variables
from eeazycrm.config_vars import *

class Config(object):
    DEBUG = False
    TESTING = False
    RBAC_USE_WHITE = True
    PYTHON_VER_MIN_REQUIRED = '3.5.0'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = DEV_SECRET_KEY  # Ensure DEV_SECRET_KEY is defined in config_vars
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DEV_DB_USER}:{DEV_DB_PASS}@{DEV_DB_HOST}/{DEV_DB_NAME}'


class TestConfig(Config):
    TESTING = True
    SECRET_KEY = TEST_SECRET_KEY  # Ensure TEST_SECRET_KEY is defined in config_vars
    SQLALCHEMY_DATABASE_URI = f'postgresql://{TEST_DB_USER}:{TEST_DB_PASS}@{TEST_DB_HOST}/{TEST_DB_NAME}'


class ProductionConfig(Config):
    SECRET_KEY = SECRET_KEY  # Ensure SECRET_KEY is defined in config_vars
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'  # Ensure DB_USER, DB_PASS, DB_HOST, and DB_NAME are defined in config_vars
