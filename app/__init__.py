# from flask import Flask, Blueprint
# from .api.v1 import version_one as v1


# def create_app(config_name):

#     app = Flask(__name__)
#     app.register_blueprint(v1)
#      return app
# gunicorn "app:create_app('debug')"

from app.api.v1.views import app

if __name__ == '__main__':
    app.run(debug=True)