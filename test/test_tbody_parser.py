import os
from unittest import TestCase

from world.world_list_parser import WorldListParser


class TestTbodyParser(TestCase):

    def test_parser_skips_tbody(self):
        html = "<tbody class='server-list__body'></tbody>"
        parser = WorldListParser()
        parser.feed(html)
        parser.close()
        self.assertEqual([], parser.get_results())

    def test_parser_parses_world_number(self):
        html = "<tbody class='server-list__body'><tr class='server-list__row'><td class='server-list__row-cell'>" \
               "<a id='slu-world-301' class='server-list__world-link' " \
               "href='https://oldschool.runescape.com/a=13/game?world=301'>Old School 1</a>" \
               "</td></tr></tbody>"
        parser = WorldListParser()
        parser.feed(html)
        parser.close()
        self.assertEqual([{
            'pvp': False,
            'number': 1,
            'player_count': None,
            'country': None,
            'type': None,
            'activity': None,
        }], parser.get_results())

    def test_parser_parses_number_over_100(self):
        html = "<tbody class='server-list__body'><tr class='server-list__row'><tr class='server-list__row'>" \
               "<td class='server-list__row-cell'>" \
               "<a id='slu-world-424' class='server-list__world-link' href='https://oldschool.runescape.com/a=13/game?world=424'>OldSchool 124</a>" \
               "</td></tr></tbody>"
        parser = WorldListParser()
        parser.feed(html)
        parser.close()
        self.assertEqual([{
            'pvp': False,
            'number': 124,
            'player_count': None,
            'country': None,
            'type': None,
            'activity': None,
        }], parser.get_results())

    def test_parser_parses_player_count(self):
        html = "<tbody class='server-list__body'><tr class='server-list__row'>" \
               "<td class='server-list__row-cell'>784 players</td>" \
               "</td></tr></tbody>"

        parser = WorldListParser()
        parser.feed(html)
        parser.close()
        self.assertEqual([{
            'pvp': False,
            'number': None,
            'player_count': 784,
            'country': None,
            'type': None,
            'activity': None,
        }], parser.get_results())

    def test_parser_parses_country(self):
        html = "<tbody class='server-list__body'><tr class='server-list__row'>" \
               "<td class='server-list__row-cell server-list__row-cell--country server-list__row-cell--US'>United States</td>" \
               "</td></tr></tbody>"

        parser = WorldListParser()
        parser.feed(html)
        parser.close()
        self.assertEqual([{
            'pvp': False,
            'number': None,
            'player_count': None,
            'country': "United States",
            'type': None,
            'activity': None,
        }], parser.get_results())

    def test_parser_parses_type(self):
        html = "<tbody class='server-list__body'><tr class='server-list__row'>" \
               "<td class='server-list__row-cell server-list__row-cell--type'>Free</td>" \
               "</td></tr></tbody>"

        parser = WorldListParser()
        parser.feed(html)
        parser.close()
        self.assertEqual([{
            'pvp': False,
            'number': None,
            'player_count': None,
            'country': None,
            'type': "free",
            'activity': None,
        }], parser.get_results())

    def test_parser_parses_activity(self):
        html = "<tbody class='server-list__body'><tr class='server-list__row'>" \
               "<td class='server-list__row-cell'>Trade - Free</td>" \
               "</td></tr></tbody>"

        parser = WorldListParser()
        parser.feed(html)
        parser.close()
        self.assertEqual([{
            'pvp': False,
            'number': None,
            'player_count': None,
            'country': None,
            'type': None,
            'activity': "Trade - Free",
        }], parser.get_results())

    def test_parser_parses_pvp_worlds(self):
        html = "<tbody class='server-list__body'>" \
               "<tr class='server-list__row server-list__row--pvp server-list__row--members'>" \
               "</tr></tbody>"

        parser = WorldListParser()
        parser.feed(html)
        parser.close()
        self.assertEqual([{
            'pvp': True,
            'number': None,
            'player_count': None,
            'country': None,
            'type': None,
            'activity': None,
        }], parser.get_results())

    def test_parser_parses_full_world(self):
        html = "<tbody class='server-list__body'>" \
               "<tr class='server-list__row server-list__row--members'>" \
               "<td class='server-list__row-cell'>" \
               "<a id='slu-world-324' class='server-list__world-link' href='https://oldschool.runescape.com/a=13/game?world=324'>Old School 24</a>" \
               "</td>" \
               "<td class='server-list__row-cell'>216 players</td>" \
               "<td class='server-list__row-cell server-list__row-cell--country server-list__row-cell--US'>United States</td>" \
               "<td class='server-list__row-cell server-list__row-cell--type'>Members</td>" \
               "<td class='server-list__row-cell'>-</td>" \
               "</tr>" \
               "</tbody>"

        parser = WorldListParser()
        parser.feed(html)
        parser.close()
        self.assertEqual([{
            'pvp': False,
            'number': 24,
            'player_count': 216,
            'country': "United States",
            'type': "members",
            'activity': "-",
        }], parser.get_results())

    def test_parser_parses_multiple_worlds(self):
        html = ""
        with open(os.path.join(os.path.dirname(__file__), 'multiple_worlds.txt'), 'r') as f:
            for line in f:
                html += line

        parser = WorldListParser()
        parser.feed(html)
        parser.close()

        expected = [
            {
                'pvp': False,
                'number': 24,
                'player_count': 216,
                'country': "United States",
                'type': "members",
                'activity': '-',
            },
            {
                'pvp': True,
                'number': 25,
                'player_count': 304,
                'country': "United Kingdom",
                'type': "members",
                'activity': 'PvP World',
            },
            {
                'pvp': False,
                'number': 26,
                'player_count': 280,
                'country': "United Kingdom",
                'type': "free",
                'activity': 'LMS Competitive',
            },
            {
                'pvp': False,
                'number': 27,
                'player_count': 855,
                'country': "Germany",
                'type': "members",
                'activity': 'Ourania Altar',
            }
        ]

        self.assertEqual(expected, parser.get_results())
