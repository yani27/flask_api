from app import app

if __name__ == '__main__':

    app.run(threaded=True, host='0.0.0.0', port=5000)
    app.config.from_pyfile('config.py')
