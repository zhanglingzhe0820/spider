# -*- coding: utf-8 -*-
from flask import (
    Flask,
    json,
    request,
    jsonify)

from bet import b

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'import_thing'
app.config['JSON_AS_ASCII'] = False


@app.route('/create', methods=['POST'])
def create():
    data = json.loads(request.data.decode('utf-8'))
    b.create(data['url'], data['username'], data['password'])
    return "success"


@app.route('/bet', methods=['POST'])
def bet():
    data = json.loads(request.data.decode('utf-8'))
    result = b.bet(data['kind'], data['multiple'], data['str'])
    return jsonify({'keys': result})


if __name__ == '__main__':
    app.run(port=8080)
