#!/usr/bin/python3
# -*- coding: utf-8 -*-

import http.client


def find_ip():
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    ip = conn.getresponse().read().decode('utf8')
    return ip


SERVER_PORT = '5000'
CLIENT_PORT = '5050'


DB_CONFIG = dict(
    provider='postgres',
    user='postgres',
    host='127.0.0.1',  # warning: choose your localhost IP
    database='avito_shortener')
