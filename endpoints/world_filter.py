from flask_restful import Resource

from filters.country_filter import CountryFilter
from filters.filter_applier import FilterApplier
from filters.member_filter import MemberFilter
from filters.player_count_max_filter import PlayerCountMaxFilter
from filters.player_count_min_filter import PlayerCountMinFilter
from filters.pvp_world_filter import PvpWorldFilter
from utils.world_utils import worlds_to_json
from world.world_fetcher import world_fetcher

applier = FilterApplier()
applier.add_filters(PvpWorldFilter, PlayerCountMaxFilter, PlayerCountMinFilter, CountryFilter, MemberFilter)


class WorldFilter(Resource):
    def get(self):
        worlds = world_fetcher.get_worlds()
        worlds = applier.apply(worlds)
        worlds_json = worlds_to_json(worlds)
        return {
            'last_update': world_fetcher.get_last_update(),
            'count': len(worlds),
            'worlds': worlds_json
        }



