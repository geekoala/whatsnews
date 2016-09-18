"""
Author: Wenhua Yang
Date: 09/18/2016

A typical authorization api for external use(tests code). Used for granting
the the authority of further resources visiting, e.g. use search api requires
a token generated by this auth_api.
"""

from flask import Flask, Response
import json

from auth_api.provider import auth_service


app = Flask(__name__)


@app.route("/token/<client_id>/<secret>")
def get_token(client_id, secret):
    """Generate token for user by calling auth_service.

    Parameters
    ----------
    client_id: string
        caller's id, a designated id for caller.
    secret: string
        a secret string corresponding with client_id.

    Returns
    -------
    return a json.
    """

    resp = auth_service.get_token(client_id, secret)
    result = json.dumps(resp)
    return Response(ret_json, mimetype='application/json')
