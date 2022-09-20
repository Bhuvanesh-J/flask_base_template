

def register_blueprint(app):
    from api.student.views import crud_blueprint
    app.register_blueprint(crud_blueprint)
    return app

