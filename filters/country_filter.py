import typing
from flask_restful import reqparse

from filters.abstract_filter import AbstractFilter


class CountryFilter(AbstractFilter):
    def filter(self):
        parser = reqparse.RequestParser()
        parser.add_argument('countries', type=str, help='[String] Allowed countries, comma separated, case ignored.')
        args = parser.parse_args()
        countries = args['countries']

        if countries:
            countries_list: typing.List[str] = countries.split(',')
            countries_list = [country.strip().casefold() for country in countries_list]

            world_list = [world for world in self._world_list if
                          world.country is not None and world.country.casefold() in countries_list]
            return world_list
        return self._world_list
