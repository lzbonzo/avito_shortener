#!/usr/bin/python3
# -*- coding: utf-8 -*-

SERVER_IP = '127.0.0.1' # warning: choose your SERVER_IP
SERVER_PORT = '5000'
SERVER_URL = f'http://{SERVER_IP}:{SERVER_PORT}'
CLIENT_IP = '127.0.0.1' # warning: choose your CLIENT_IP
CLIENT_PORT = '5050'


DB_CONFIG = dict(
    provider='postgres',
    user='postgres',
    host='127.0.0.1', # warning: choose your localhost IP
    database='avito_shortener')
