from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("config.cfg", silent=True)

    if test_config:
        app.config.from_mapping(test_config)

    from . import home
    app.register_blueprint(home.bp)

    return app
