from flask import Flask, request
import time
import zmq

HOST = '127.0.0.1'
PORT = '4444'

_context = zmq.Context()
_publisher = _context.socket(zmq.PUB)
url = 'tcp://{}:{}'.format(HOST, PORT)

def publish_message(message):

    try:
        _publisher.bind(url)
        time.sleep(1)
        print("sending message : {0}".format(message, _publisher))
        _publisher.send(message.encode('ascii'))

    except Exception as e:
        raise
        print("error {0}".format(e))

    finally:
        print("unbinding")
        _publisher.unbind(url)

# == [ APP FACTORY ] == #
def create_app():

    # == [ APP ] == #
    app = Flask(__name__, static_url_path='/static')

    @app.route("/")
    def index():
        return "Flask App inside Docker!!"

    @app.route("/events")
    def events():
        _strn = request.args.get('param')
        response = 'lower case of {} is {}'.format(_strn, _strn.lower())
        publish_message(response)
        return response

    @app.route("/places")
    def places():
        _strn = request.args.get('param')
        response = 'lower case of {} is {}'.format(_strn, _strn.lower())
        publish_message(response)
        return response

    @app.route("/loaderio-6a1867014e730/")
    def loaderio():
        return app.send_static_file("loaderio-6a1867014e730.txt")

    return app