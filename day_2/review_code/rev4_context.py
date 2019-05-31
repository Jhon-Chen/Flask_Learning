from flask import Flask, current_app, request, g

app = Flask(__name__)


@app.route('/')
def index():
    print(current_app.__name__)
    print(request.url)
    g.name = 'text programme'
    print(g.name)
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)