from api.student.views import crud_blueprint


def register_blueprint(app):
    app.register_blueprint(crud_blueprint)
    return app

