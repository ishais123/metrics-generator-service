import os
from prometheus_flask_exporter import PrometheusMetrics
from flask import (
    Flask,
    jsonify,
    Response,
    request
)

DEFAULT_PORT: int = 5001
DEFAULT_HOST: str = '0.0.0.0'

APP_PORT: int = os.environ['APP_PORT'] if 'APP_PORT' in os.environ else DEFAULT_PORT
APP_HOST: str = os.environ['APP_HOST'] if 'APP_HOST' in os.environ else DEFAULT_HOST

APP_ROUTES: dict = {
    "alive": "/alive",
    "health": "/health"
}


class MetricsGeneratorError(BaseException):
    """Raise for metrics generator service exceptions"""


if __name__ == '__main__':

    try:
        app: Flask = Flask(__name__)
        metrics: PrometheusMetrics = PrometheusMetrics(app)

        by_path_counter = metrics.counter(
            'by_path_counter', 'Request count by request paths',
            labels={'path': lambda: request.path}
        )


        @app.route(APP_ROUTES.get('health'))
        @by_path_counter
        def health() -> tuple[Response, int]:
            return jsonify({"healthy": "true"}), 200


        @app.route(APP_ROUTES.get('alive'))
        @by_path_counter
        def alive() -> tuple[Response, int]:
            return jsonify({"alive": "true"}), 200


        app.run(host=APP_HOST, port=APP_PORT)

    except Exception as e:
        raise MetricsGeneratorError(f'Failed to run metrics generator service due the following error: {e}')
