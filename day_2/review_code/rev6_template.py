from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/demo')
def demo():
    my_list = [1, 2, 4, 6]
    my_data = 'let me go'
    my_word = '<h2>"I am the bone of my sword. Steel is my body, and fire is my blood. I have created over a thousand " \
              "blades. Unknown to Death. Nor known to Life. Have withstood pain to create many weapons. Yet, " \
              "those hands will never hold anything. So as I pray, Unlimited Blade Works. "</h2>'
    return render_template('rev6_template.html', a=my_list, b=my_data, c=my_word)


@app.template_filter('my_reverse')
def my_reverse(word):
    temp = list(word)
    temp.reverse()
    return temp


if __name__ == '__main__':
    app.run(debug=True)