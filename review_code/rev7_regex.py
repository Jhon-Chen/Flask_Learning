from flask import Flask
from werkzeug.routing import BaseConverter


class RegexConvert(BaseConverter):
    def __init__(self, url_map, *args):
        super(RegexConvert, self).__init__(url_map)
        self.regex = args[0]


app = Flask(__name__)
app.url_map.converters['re'] = RegexConvert


@app.route('/')
def index():
    return 'index'


@app.route('/user/<re("[0-9]{3}"):user_id>')
def user_info(user_id):
    return "user_id为 %s" % user_id


if __name__ == '__main__':
    app.run(debug=True)