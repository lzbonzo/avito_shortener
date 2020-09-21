#!/usr/bin/python3
# -*- coding: utf-8 -*-

import http.client


def find_ip():
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    ip = conn.getresponse().read().decode('utf8')
    return ip


SERVER_IP = '127.0.0.1' # warning: choose your SERVER_IP
PORT = '5000'
SERVER_URL = f'http://{SERVER_IP}:{PORT}'
CLIENT_IP = '127.0.0.1' # warning: choose your CLIENT_IP
CLIENT_PORT = '5050'


DB_CONFIG = dict(
    provider='postgres',
    user='postgres',
    host='127.0.0.1', # warning: choose your localhost IP
    database='avito_shortener')
