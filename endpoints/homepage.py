from collections import OrderedDict

from flask_restful import Resource

import flask_app


class Homepage(Resource):
    def get(self):
        rules = {}
        for rule in flask_app.app.url_map.iter_rules():
            rules[rule.endpoint] = str(rule)

        return {
            'routes': OrderedDict(sorted(rules.items(), key=lambda rule: rule[0]))
        }, 200, {'Access-Control-Allow-Origin': '*'}
