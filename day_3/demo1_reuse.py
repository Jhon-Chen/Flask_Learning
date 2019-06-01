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




if __name__ == '__main__':
    app.run()
