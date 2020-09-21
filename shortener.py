#!/usr/bin/python3
# -*- coding: utf-8 -*-

import hashlib
from flask import Flask, request, redirect
import settings
from models import Urls
from pony.orm import db_session
import requests

app = Flask(__name__)


@app.route('/')
def html_doc():
    return {'shortener': 'OK'}


@app.route('/', methods=['POST'])
@db_session
def short():
    full_url = request.form.get('full_url').strip().lower()
    if not full_url.startswith('http'):
        full_url = f'http://{full_url}'
        try:
            requests.get(full_url)
        except Exception as err:
            return {'short': 'Указанный Вами ресурс недоступен'}
    url = Urls.get(full_url=full_url)
    if url is None:
        short_url = shortener(full_url)
        short_json = {'short': short_url}
    else:
        short_json = {'short': f'{settings.SERVER_URL}/{url.hashed_url}'}
    return short_json


@app.route('/<hashed_url>', methods=['GET'])
@db_session
def redirect_url(hashed_url):
    full_url = Urls.get(hashed_url=hashed_url)
    return redirect(full_url.full_url)


@db_session
def shortener(url):
    hashed_url = hashlib.md5(url.encode()).hexdigest()[:8]
    Urls(hashed_url=hashed_url, full_url=url)
    short_url = f'{settings.SERVER_URL}/{hashed_url}'
    return short_url


if __name__ == '__main__':
    IP = settings.find_ip()
    SERVER_URL = f'http://{IP}:{settings.PORT}'
    app.run(host=IP, port=settings.PORT)
