from flask_restful import Resource

from utils.world_utils import worlds_to_json
from world.world_fetcher import world_fetcher


class WorldList(Resource):
    def get(self):
        worlds = world_fetcher.get_worlds()
        worlds_json = worlds_to_json(worlds)
        return {
            'last_update': world_fetcher.get_last_update(),
            'count': len(worlds),
            'worlds': worlds_json
        }, 200, {'Access-Control-Allow-Origin': '*'}
