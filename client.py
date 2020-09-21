#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from flask import Flask, render_template, request
import settings

client = Flask(__name__)


@client.route('/')
def html_doc():
    return render_template('index.html')


@client.route('/', methods=['POST'])
def take_full_url():
    full_url = request.form.get('full_url').strip()
    SERVER_URL = f'http://{IP}:{settings.PORT}'
    if full_url:
        short_json = requests.post(SERVER_URL, data={'full_url': full_url}).json()
        return render_template('short.html', short_json=short_json)
    return render_template('index.html')


if __name__ == "__main__":
    IP = '127.0.0.1'
    client.run(host=IP, port=settings.CLIENT_PORT)
