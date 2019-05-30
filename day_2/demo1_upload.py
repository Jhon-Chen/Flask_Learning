from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/upload', methods=['post'])
def upload():
    file = request.files.get('pic')
    file.save('1.gif')
    return 'success'


if __name__ == '__main__':
    app.run(host='192.168.211.128', debug=True)