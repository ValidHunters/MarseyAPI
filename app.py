from flask import Flask

from api.v1 import create_api_blueprint

app = Flask(__name__)

# Register the API blueprint
api_blueprint = create_api_blueprint()
app.register_blueprint(api_blueprint, url_prefix='/api/v1')


def run_app():
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)


if __name__ == '__main__':
    run_app()
    