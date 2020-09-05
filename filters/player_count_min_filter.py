from flask_restful import reqparse

from filters.abstract_filter import AbstractFilter


class PlayerCountMinFilter(AbstractFilter):
    def filter(self):
        parser = reqparse.RequestParser()
        parser.add_argument('player_count_min', type=int, help='[Integer] Min allowed player count (inclusive).')
        args = parser.parse_args()
        min_players = args['player_count_min']

        if min_players:
            world_list = [world for world in self._world_list if
                          world.player_count is not None and world.player_count >= min_players]
            return world_list
        return self._world_list
