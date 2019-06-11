from flask import Flask, render_template, session, g, flash

app = Flask(__name__)
app.secret_key = 'asdqwezxc'


@app.route('/')
def index():
    return 'index'


@app.route('/demo1')
def demo1():
    session['name'] = "gakki"
    g.name = 'jhonchen'
    flash("闪现")

    return render_template('temp4_special.html')


if __name__ == '__main__':
    app.run(debug=True)