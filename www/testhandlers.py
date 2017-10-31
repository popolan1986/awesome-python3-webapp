import asyncio
from coroweb import get, post

# URL handler used in the test
@get('/')
async def handler_url_blog(request):
    body='<h1>tlan is awesome</h1>'
    return body

@get('/greeting')
async def handler_url_greeting(*, name, request):
    body='<h1>tlan is awesome: /greeting %s</h1>' %name
    return body
