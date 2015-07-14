import sys
import os

sys.path.append(os.path.dirname(__file__))  # adding src directory to path


def setup_application():
    from anillo.app import application
    from anillo.utils import chain
    from anillo.middlewares.params import get_params_middleware
    from anillo.middlewares.json import json_middleware
    from anillo.middlewares.default_headers import default_headers_middleware
    from router import router
    handler = chain(
        get_params_middleware,
        json_middleware,
        default_headers_middleware({}, {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}),
        router
    )
    return application(handler)


if __name__ == '__main__':
    from anillo import serving
    app = setup_application()
    serving.run_simple(app, port=5000, host='0.0.0.0')
