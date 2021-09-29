import time
import typing
from threading import Thread

import requests

from influx_db_handler.word_data_populator import WorldDataPopulator
from utils.session_creator import SessionCreator
from world.world_data_extractor import WorldDataExtractor


class WorldFetcher(Thread):
    """Fetches the world list from the OSRS website"""

    _world_data_url = "https://oldschool.runescape.com/a=13/slu"

    def __init__(self, interval=10, proxy=None):
        """
        :interval The interval to download data in seconds
        """
        super().__init__()
        self.setDaemon(True)
        self._running = True
        self._interval = interval
        self._proxy = proxy
        self._session = None
        self._worlds = []
        self._last_update = None

    def run(self) -> None:
        while self._running:
            response = self._fetch()
            self._last_update = int(time.time())
            if response:
                data_extractor = WorldDataExtractor(response.text)
                data_extractor.extract()
                self._worlds = data_extractor.get_worlds()
                WorldDataPopulator().populate_world_data(self._worlds)
            time.sleep(self._interval)

    def get_worlds(self) -> typing.List:
        return self._worlds[:]

    def get_last_update(self) -> int:
        return self._last_update

    def _fetch(self) -> (requests.Response, None):
        session = self._get_session()
        response = session.get(self._world_data_url)
        if response.status_code == 200:
            return response
        else:
            return None

    def _get_session(self) -> requests.Session:
        if not self._session:
            self._session = SessionCreator.create(self._proxy)
        return self._session


world_fetcher = WorldFetcher()
