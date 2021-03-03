from flask_classful import FlaskView
from flask import redirect, render_template


class DetectorMiddleware(FlaskView):
    def __init__(self):
        self.form = None

    def before_post(self):
        pass

    def before_get(self):
        pass
