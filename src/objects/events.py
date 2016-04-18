from flask import Flask, jsonify, make_response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return make_response(jsonify({"message": "Hello Events"}), 200)

if __name__ == '__main__':
    #app.run()
    app.run(host='127.0.0.1', port=4444, debug=True)