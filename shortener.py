#!/usr/bin/python3
# -*- coding: utf-8 -*-
import hashlib
from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
def html_doc():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def short():
    full_url = request.form.get('full_url')
    short_url = shortener(full_url)
    return {'short': short_url}


@app.route('/<hashed_url>', methods=['GET'])
def redir(hashed_url):
    if hashed_url in short_urls:
        return redirect(short_urls[hashed_url])


def shortener(url):
    hashed_url = hashlib.md5(url.encode()).hexdigest()[:8]
    short_urls[hashed_url] = url
    short_url = f'{SERVER_IP}/{hashed_url}'
    return short_url


SERVER_IP = 'http://127.0.0.1:5000'
short_urls = {}

if __name__ == '__main__':
    app.run()
