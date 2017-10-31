from aiohttp import web
import asyncio
from coroweb import add_routes, add_static
from app import init_jinja2, datetime_filter, logger_factory, response_factory
import logging; logging.basicConfig(level=logging.INFO)

# web test app
async def init(loop):
    app = web.Application(loop=loop, middlewares=[logger_factory, response_factory])
    init_jinja2(app, filters=dict(datetime=datetime_filter), path=r"G:\\Users\\tlan.NI\\Documents\\py\\awesome-python3-webapp\www\\templates")
    add_routes(app, 'testhandlers')
    add_static(app)
    srv = await loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('Server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()