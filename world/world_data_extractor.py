import typing

from world.world_list_parser import WorldListParser
from world.world import World


class WorldDataExtractor:
    """
    Goes through the HTML of the OSRS world list page and extracts the details of each world.
    """
    def __init__(self, text):
        self._text = text
        self._worlds = []

    def extract(self) -> None:
        """Extract the worlds data"""
        tbody = self._extract_tbody(self._text)
        parser = WorldListParser()
        parser.feed(tbody)
        parser.close()
        worlds_data = parser.get_results()
        worlds = []

        for world_data in worlds_data:
            world = World(world_data)
            worlds.append(world)

        self._worlds = worlds

    def get_worlds(self) -> typing.List[dict]:
        """Get the list of worlds"""
        return self._worlds

    def _extract_tbody(self, text) -> (str, None):
        """
        Tries to extract the tbody tag from the source html
        :return str if it's successful, None otherwise
        """
        start_index = -1
        stop_index = -1
        text_list = text.split('\n')
        for index, line in enumerate(text_list):
            if start_index == -1 and "<tbody class='server-list__body'>" in line:
                start_index = index

            if start_index != -1 and "</tbody>" in line:
                stop_index = index

            if start_index != -1 and stop_index != -1:
                break

        if start_index != -1 and stop_index != -1:
            return '\n'.join(text_list[start_index:stop_index])
        return None
