from flask import Flask, render_template
from flask_sock import Sock
from lexicon import lexicon
from search import search_lexicon
import json


app = Flask(__name__)
sock = Sock(app)


@app.route('/')
def index():
    return render_template('index.html')


@sock.route('/echo')
def echo(sock):
    while True:
        query = sock.receive()
        result = search_lexicon(query, lexicon=lexicon)
        sock.send(json.dumps(result[:20]))