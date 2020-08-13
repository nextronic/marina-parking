from flask_classful import FlaskView


class MapMiddleware(FlaskView):
    def __init__(self):
        self.form = None

    def before_post(self):
        pass

    def before_get(self):
        pass
