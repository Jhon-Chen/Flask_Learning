from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/demo1')
def demo1():
    my_int = 10
    my_str = '<h1>enheng<h1>'
    my_list = [1, 4, 5]
    my_dict = {
        'da': 1,
        'se': 'asd'
    }
    return render_template('demo6_template.html',
                           a=my_int,
                           b=my_str,
                           c=my_list,
                           d=my_dict)


if __name__ == '__main__':
    app.run(debug=True)