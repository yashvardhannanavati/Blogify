# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask import jsonify, Blueprint

from blogify import version
from blogify.databases import client


api_v1 = Blueprint('api_v1', __name__)
db = client.blogify_db

@api_v1.route('/about')
def about():
    """
    Display version info about blogify
    :return: A JSON object with version info
    """
    return jsonify({'version': version})
