from V1App import create_app

app = create_app('config')

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8080, debug=True)
    app.run()
