from collections import OrderedDict
from os import getenv, path

from flask import Flask, request
from flask_restful import Resource, Api
from dotenv import load_dotenv

from world.world_fetcher import WorldFetcher

load_dotenv()
app = Flask("WorldGuardian")
api = Api(app)

world_fetcher = WorldFetcher()
world_fetcher.start()

with open(path.join(path.dirname(__file__), 'version'), 'r') as f:
    version = f.readline()


class WorldList(Resource):
    def get(self):
        worlds = world_fetcher.get_worlds()
        worlds_json = sorted([world.to_dict() for world in worlds], key=lambda world: world['number'])
        return {
            'last_update': world_fetcher.get_last_update(),
            'worlds': worlds_json
        }


class WorldFilter(Resource):
    def get(self):
        print(request.args)


class Homepage(Resource):
    def get(self):
        rules = {}
        for rule in app.url_map.iter_rules():
            rules[rule.endpoint] = str(rule)

        return {
            'routes': OrderedDict(sorted(rules.items(), key=lambda rule: rule[0]))
        }


class Info(Resource):
    def get(self):
        return {
            'author': "Downsidelama@Lugalbanda",
            'github': "https://github.com/lugalbandars/world-guardian",
            'version': version,
            'lugalbanda': {
                'website': 'https://lugalbanda.com/',
                'info': "All in one bot farm automatization solution for an affordable price! "
                        "This project is an open source part of the service."
            },
            'license': "https://github.com/lugalbandars/world-guardian/LICENSE.md",
        }


api.add_resource(Homepage, '/', endpoint='homepage')
api.add_resource(WorldList, '/worlds', endpoint='world-list')
api.add_resource(WorldFilter, '/worlds/filter', endpoint='world-filter')
api.add_resource(Info, '/info', endpoint='info')

if __name__ == "__main__":
    debug_mode = getenv('debug', False)
    app.run(debug=debug_mode)
