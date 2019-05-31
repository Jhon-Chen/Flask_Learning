from flask import Flask
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        self.regex = args[0]

    def to_python(self, value):
        return int(value) + 10000


app = Flask(__name__)
app.url_map.converters['py'] = RegexConverter


@app.route('/')
def index():
    return 'index'


@app.route('/user/<py("[0-9]{3}"):user_id>')
def user_info(user_id):
    return "%s" % user_id


if __name__ == '__main__':
    app.run(debug=True)