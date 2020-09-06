from os import getenv

from dotenv import load_dotenv

from flask_app import app, api
from endpoints.homepage import Homepage
from endpoints.info import Info
from endpoints.world_filter import WorldFilter
from endpoints.world_list import WorldList
from world.world_fetcher import world_fetcher

load_dotenv()

world_fetcher.start()
debug_mode = getenv('debug', False)
api.add_resource(WorldFilter, '/worlds/filter', endpoint='world-filter')
api.add_resource(WorldList, '/worlds', endpoint='world-list')
api.add_resource(Info, '/info', endpoint='info')
api.add_resource(Homepage, '/', endpoint='homepage')

if __name__ == "__main__":
    app.run()
