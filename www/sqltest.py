import orm, asyncio
from models import User, Blog, Comment

async def test_save(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    u = User(name='Test1', email='123@example.com', passwd='1234567890', image='about:blank')
    await u.save()

# get message loop
loop = asyncio.get_event_loop()
loop.run_until_complete(test_save(loop))
__pool.close()
loop.run_until_complete(__pool.wait_closed())
loop.close()

