from flask_classful import FlaskView


class UsersMiddleware(FlaskView):
    def __init__(self):
        self.form = None

    def before_post(self):
        pass

    def before_delete(self, id):
        #tmp = Queue.query.filter_by(id_queue=id).first()
        #if tmp is None:
        #    return "", 404
        pass
