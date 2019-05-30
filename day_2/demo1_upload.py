from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/upload', methods=['post'])
def upload():
    """request.args
    request.data
    request.url
    request.method"""
    file = request.files.get('pic')
    file.save('1.gif')
    return 'success'


@app.route('/data', methods=['post'])
def data():
    data = request.data
    print(data)
    return "OK"


if __name__ == '__main__':
    app.run(host='192.168.211.128', debug=True)

    """Address already in use
    ubuntu : netstat -apn |grep 5000
    kill -9 pid"""