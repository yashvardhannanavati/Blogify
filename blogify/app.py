# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

import os

from flask import Flask
from werkzeug.exceptions import default_exceptions

from blogify.logger import init_logging
from blogify.error import json_error, ValidationError
from blogify.api.v1 import api_v1

def load_config(app):
    default_config_file = None
    if os.getenv('DEV') and os.getenv('DEV').lower() == 'true':
        default_config_obj = 'blogify.config.DevConfig'
    else:
        default_config_obj = 'blogify.config.ProdConfig'
        default_config_file = '/etc/blogify/settings.py'

    app.config.from_object(default_config_obj)
    config_file = os.environ.get('BLOGIFY_CONFIG', default_config_file)
    if config_file:
        app.config.from_pyfile(config_file)

    if os.environ.get('SECRET_KEY'):
        app.config['SECRET_KEY'] = os.environ['SECRET_KEY']


def create_app(config_obj=None):
    app = Flask(__name__)
    if config_obj:
        app.config.from_object(config_obj)
    else:
        load_config(app)

    if app.config['PRODUCTION'] and app.secret_key == 'replace-me-with-something-random':
        raise Warning('You need to change the app.secret_key value for production')

    init_logging(app)

    for status_code in default_exceptions.keys():
        app.register_error_handler(status_code, json_error)
    app.register_error_handler(ValidationError, json_error)
    app.register_blueprint(api_v1, url_prefix='/api/v1')

    return app