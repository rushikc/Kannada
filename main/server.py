# coding=utf-8
import random
from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    texts = str(name)
    k2 = texts.replace("\n", "").replace("\r", "")
    file = open("data/comment.txt", "a+")
    file.writelines(k2)
    file.writelines('\n')
    file.close()

    return 'Comment Entered By User: %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))

    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)
