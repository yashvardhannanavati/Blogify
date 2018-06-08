# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals


class Config(object):
    """
    A Blogify Flask configuration
    """
    DEBUG = True
    # We configure logging explicitly, turn off the Flask-supplied log handler.
    LOGGER_HANDLER_POLICY = 'never'
    HOST = '0.0.0.0'
    PRODUCTION = False
    SHOW_DB_URI = False
    SECRET_KEY = 'replace-me-with-something-random'
    MONGO_URI = 'mongodb://<username>:<password>@localhost/blogify_db'

class ProdConfig(Config):
    DEBUG = False
    PRODUCTION = True


class DevConfig(Config):
    MONGO_DBNAME = 'blogify_db'
    MONGO_URI = 'mongodb://<username>:<password>@localhost/blogify_db'
    pass

class TestConfig(Config):
    pass