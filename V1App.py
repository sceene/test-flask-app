from flask import Flask, jsonify, make_response
import requests

# == [ APP FACTORY ] == #
def create_app():

    # == [ APP ] == #
    app = Flask(__name__, static_url_path='/static')

    @app.route("/")
    def index():
        return "Flask App inside Docker!!"

    @app.route("/events")
    def events():
        qry = 'tcp://127.0.0.1:4444'
        r = requests.get(qry)  # first call to get pages
        if r.status_code != 200:
            print('>>>ERROR: events failed.')

        response = r.json()
        return make_response(jsonify(response), 200)

    @app.route("/places")
    def places():
        qry = 'tcp://127.0.0.1:4443'
        r = requests.get(qry)  # first call to get pages
        if r.status_code != 200:
            print('>>>ERROR: places failed.')

        response = r.json()
        return make_response(jsonify(response), 200)

    @app.route("/loaderio-6a1867014e730/")
    def loaderio():
        return app.send_static_file("loaderio-6a1867014e730.txt")

    return app