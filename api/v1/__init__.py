from flask import Blueprint
from .views import *

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)


def create_api_blueprint():
    blueprint = Blueprint('v1', __name__)

    versionview = limiter.limit("15 per minute")(MarseyVersion)

    blueprint.add_url_rule('/marsey', 'marsey', MarseyHello)
    blueprint.add_url_rule('/version', 'version', versionview)
    return blueprint
