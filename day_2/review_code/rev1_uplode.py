from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


# 记录请求上传的文件
@app.route('/upload', methods=['POST'])
def upload():
    pic = request.files.get('pic')
    pic.save('./1.png')
    return 'success'


# 记录请求的数据并转换为字符串
@app.route('/data')
def data():
    data = request.data
    print(data)
    return 'OK 1'


# 记录请求中的url
@app.route('/url')
def url():
    url = request.url
    print(url)
    return 'ok 2'


if __name__ == '__main__':
    app.run(host='192.168.211.130', port=5200, debug=True)