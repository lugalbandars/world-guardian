from flask_restful import reqparse

from filters.abstract_filter import AbstractFilter


class PlayerCountMaxFilter(AbstractFilter):
    def filter(self):
        parser = reqparse.RequestParser()
        parser.add_argument('player_count_max', type=int, help='[Integer] Max allowed player count (inclusive).')
        args = parser.parse_args()
        max_players = args['player_count_max']

        if max_players:
            world_list = [world for world in self._world_list if
                          world.player_count is not None and world.player_count <= max_players]
            return world_list
        return self._world_list
