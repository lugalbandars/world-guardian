import typing
from abc import ABC, abstractmethod

from world.world import World


class AbstractFilter(ABC):
    """
    Derive all filters from here

    Use reqparse.RequestParser() to parse parameters from the request.
    Example:
        parser = reqparse.RequestParser()
        parser.add_argument('pvp', type=inputs.boolean, help='[Boolean] PvP worlds allowed or not.')
        args = parser.parse_args()
    """

    def __init__(self, world_list: typing.List[World]):
        self._world_list = world_list

    @abstractmethod
    def filter(self):
        pass
