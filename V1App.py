from flask import Flask, make_response, jsonify


# == [ APP FACTORY ] == #
def create_app(config):

    # == [ APP ] == #
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Sceene inside Docker!!"

    # == [ ERRORS ] == #
    @app.errorhandler(400)
    def bad_syntax(error):
        if 'message' in error.description:
            return make_response(jsonify({'error': '400', 'message': error.description['message']}), 400)
        else:
            return make_response(jsonify({'error': '400', 'message': 'Bad Syntax - The request cannot be fulfilled due to bad syntax'}), 400)

    @app.errorhandler(401)
    def not_authorized(error):
        if 'message' in error.description:
            return make_response(jsonify({'error': '401', 'message': error.description['message']}), 401)
        else:
            return make_response(jsonify({'error': '401', 'message': 'Unauthorized - You are unauthorized to access this data'}), 401)

    @app.errorhandler(403)
    def not_authorized(error):
        return make_response(jsonify({'error': '403', 'message': 'Unauthorized - You\'re app is not authorized to access this data'}), 403)

    @app.errorhandler(404)
    def page_not_found(error):
        if 'message' in error.description:
            return make_response(jsonify({'error': '404', 'message': error.description['message']}), 404)
        else:
            return make_response(jsonify({'error': '404', 'message': 'Not Found - The requested resource could not be found'}), 404)

    @app.errorhandler(405)
    def not_authorized(error):
        return make_response(jsonify({'error': '405', 'message': 'Method Not Allowed - That method is not allowed'}), 405)

    @app.errorhandler(409)
    def resource_conflict(error):
        if 'message' in error.description:
            return make_response(jsonify({'error': '409', 'message': error.description['message']}), 409)
        else:
            return make_response(jsonify({'error': '409', 'message': 'Conflict - The request could not be completed due to a conflict with the current state of the resource'}), 409)

    @app.errorhandler(415)
    def unsupported_media_type(error):
        return make_response(jsonify({'error': '415', 'message': 'Unsupported Media Type'}), 415)

    @app.errorhandler(500)
    def internal_error(error):
        return make_response(jsonify({'error': '500', 'message': 'Internal Server Error - Something went wrong on our end while attempting to process your request'}), 500)

    @app.errorhandler(502)
    def service_unavailable(error):
        return make_response(jsonify({'error': '502', 'message': 'Service Unavailable - Server is currently unable to handle the request due to maintenance or overload of the server'}), 502)

    @app.errorhandler(503)
    def service_unavailable(error):
        return make_response(jsonify({'error': '503', 'message': 'Service Unavailable - Server is currently unable to handle the request due to maintenance or overload of the server'}), 503)

    return app

