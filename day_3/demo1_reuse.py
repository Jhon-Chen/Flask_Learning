from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/demo1')
def demo1():
    return render_template('temp1_macro.html')


@app.route('/demo2')
def demo2():
    list1 = [1, 2, 4]
    return render_template('temp2_extend.html', a=list1)


@app.route('/demo3')
def demo3():
    return render_template('index.html')


@app.route('/demo4')
def demo4():
    return render_template('detail.html')


@app.route('/demo5')
def demo5():
    return render_template('temp3_include.html')


if __name__ == '__main__':
    app.run()
