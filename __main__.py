from os import getenv

from dotenv import load_dotenv

import flask_app
from endpoints.homepage import Homepage
from endpoints.info import Info
from endpoints.world_filter import WorldFilter
from endpoints.world_list import WorldList
from world.world_fetcher import world_fetcher

load_dotenv()

if __name__ == "__main__":
    world_fetcher.start()
    debug_mode = getenv('debug', False)
    flask_app.api.add_resource(WorldFilter, '/worlds/filter', endpoint='world-filter')
    flask_app.api.add_resource(WorldList, '/worlds', endpoint='world-list')
    flask_app.api.add_resource(Info, '/info', endpoint='info')
    flask_app.api.add_resource(Homepage, '/', endpoint='homepage')
    flask_app.app.run(debug=debug_mode)
