import typing

from filters.abstract_filter import AbstractFilter


class FilterApplier:

    def __init__(self):
        self._world_filters: typing.List[typing.Type[AbstractFilter]] = []

    def add_filter(self, world_filter):
        self._world_filters.append(world_filter)

    def add_filters(self, *world_filters):
        for world_filter in world_filters:
            self.add_filter(world_filter)

    def apply(self, worlds):
        for world_filter in self._world_filters:
            worlds = world_filter(worlds).filter()
        return worlds
