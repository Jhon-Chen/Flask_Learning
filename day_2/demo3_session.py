from flask import Flask, session

app = Flask(__name__)
# 使用session的话需要配置secret_key
app.config['SECRET_KEY'] = '15751002326Cyf'


@app.route('/')
def index():
    user_id = session['user_id', '']
    user_name = session['user_name', '']
    return "%s \r\n%s" % (user_id, user_name)


@app.route('/login')
def login():
    # 假装校验成功
    session['user_id'] = 1
    session['user_name'] = 'gakki'
    return 'success'


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)