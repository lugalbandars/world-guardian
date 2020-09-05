from flask_restful import reqparse, inputs

from filters.abstract_filter import AbstractFilter


class PvpWorldFilter(AbstractFilter):
    def filter(self):
        parser = reqparse.RequestParser()
        parser.add_argument('pvp', type=inputs.boolean, help='[Boolean] PvP worlds allowed or not.')
        args = parser.parse_args()

        if args['pvp']:
            is_pvp = args['pvp']
            world_list = [world for world in self._world_list if world.pvp == is_pvp]
            return world_list
        else:
            return self._world_list
