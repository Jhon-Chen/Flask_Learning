from flask import Flask, request, session, current_app, g
# request, session：请求上下文中的变量
# current_app, g：应用上下文的变量

app = Flask(__name__)

# print(request.method)
# working outside of request错误 因为不在请求上下文中
# print(session.get('user_id', ''))  也报错
# print(current_app.config.get('DEBUG'))


@app.route('/')
def index():
    # print(request.method) 在这里是能够获取到的
    print(current_app.config.get('DEBUG'))
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)