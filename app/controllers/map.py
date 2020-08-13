from flask_login import login_required
from ..middleware.map import MapMiddleware
from flask import render_template


class MapController(MapMiddleware):
    route_base = '/'
    decorators = [login_required]

    def index(self):
        return render_template('map.jinja2')