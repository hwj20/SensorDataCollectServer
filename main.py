import os

from flask import Flask, request, flash, url_for, Response
import pprint

from werkzeug.utils import redirect, secure_filename

UPLOAD_FOLDER = ''
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class LoggingMiddleware(object):
    def __init__(self, app):
        self._app = app

    def __call__(self, env, resp):
        errorlog = env['wsgi.errors']
        pprint.pprint(('REQUEST', env), stream=errorlog)

        def log_response(status, headers, *args):
            pprint.pprint(('RESPONSE', status, headers), stream=errorlog)
            return resp(status, headers, *args)

        return self._app(env, log_response)


@app.route('/', methods=['POST'])
def result():
    data = request.get_data()
    data = bytes.decode(data)
    print(data)
    data_file.write(data)
    data_file.flush()

    return Response("", status=200, mimetype='application/json')


data_filename = './data_collected/data.csv'
data_file = open(data_filename, 'a')
if __name__ == '__main__':
    app.wsgi_app = LoggingMiddleware(app.wsgi_app)
    # app.run(host='192.168.1.109', port=8000)
    app.run(host='10.252.135.198', port=8000, debug=True)

    data_file.close()
