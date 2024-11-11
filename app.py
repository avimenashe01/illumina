from flask import Flask
from svc.controller.store_controller import store_controller


def create_app(testing=False):
    """Factory function to create and configure the Flask app."""

    app = Flask(__name__)

    if testing:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False

    app.register_blueprint(store_controller, url_prefix='/api/store')

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
