from html.parser import HTMLParser

import typing


class WorldListParser(HTMLParser):
    """
    Parses the world list and return a list with world data dictionaries
    """

    def __init__(self, ):
        super().__init__()
        self._results = []
        self._current = None
        self._current_value = None
        self._parsing = False

    def get_results(self) -> typing.List[dict]:
        return self._results

    def handle_starttag(self, tag, attrs):
        if tag == 'tbody':
            self._parsing = True

        if self._parsing:
            if tag == 'tr':
                self._parse_tr_tag(attrs)

            if tag == 'a':
                self._current_value = 'number'

            if tag == 'td':
                self._parse_td_tag(attrs)

    def _parse_tr_tag(self, attrs):
        pvp = False
        for attribute in attrs:
            if 'class' in attribute[0]:
                if 'pvp' in attribute[1]:
                    pvp = True
        self._current = {
            'pvp': pvp,
            'number': None,
            'player_count': None,
            'country': None,
            'type': None,
            'activity': None,
        }

    def _parse_td_tag(self, attrs):
        for attribute in attrs:
            if attribute[0] == 'class':
                if 'country' in attribute[1]:
                    self._current_value = 'country'
                    break
                elif 'type' in attribute[1]:
                    self._current_value = 'type'
                    break
                else:
                    if self._current['player_count'] is not None:
                        self._current_value = 'activity'

    def handle_endtag(self, tag):
        if tag == 'tbody':
            self._parsing = False

        elif tag == 'tr':
            self._results.append(self._current)

    def handle_data(self, data: str):
        if self._current_value is None:
            # Either player_count or activity
            # Determining it without previous data
            # A column might be missing, although very unlikely

            if 'players' in data:
                self._current_value = 'player_count'
            else:
                self._current_value = 'activity'

        if self._current_value == 'number':
            self._current['number'] = int(data.replace('Old School ', '').replace('OldSchool ', ''))
            self._current_value = None

        elif self._current_value == 'player_count':
            self._current['player_count'] = int(data.replace(' players', ''))
            self._current_value = None

        elif self._current_value == 'country':
            self._current['country'] = data
            self._current_value = None

        elif self._current_value == 'type':
            self._current['type'] = data.lower()
            self._current_value = None

        elif self._current_value == 'activity':
            if data.strip() != "":
                self._current['activity'] = data
            self._current_value = None

    def error(self, message):
        pass
