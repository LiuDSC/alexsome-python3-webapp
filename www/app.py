# !user/bin/env python3
#  -*- coding: utf-8 -*-

__author__ = 'Alex LIU'

'''
async web application.
'''

from aiohttp import web

async def index(request):
    return web.Response(body= b"<h1>Awesome!</h1>", headers = {"content-type": "text/html"})

app = web.Application()
app.add_routes([web.get('/', index)])
web.run_app(app, host='127.0.0.1', port=9090)