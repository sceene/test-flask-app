from flask import Flask


# == [ APP FACTORY ] == #
def create_app():

    # == [ APP ] == #
    app = Flask(__name__, static_url_path='/static')

    @app.route("/")
    def index():
        return "Flask App inside Docker!!"

    @app.route("/loaderio-6a1867014e730/")
    def loaderio():
        return app.send_static_file("loaderio-6a1867014e730.txt")

    return app

