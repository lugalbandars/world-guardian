from os import path

from flask_restful import Resource
from definitions import ROOT_DIRECTORY

with open(path.join(ROOT_DIRECTORY, 'version'), 'r') as f:
    version = f.readline()


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
            'license': "https://github.com/lugalbandars/world-guardian/blob/master/LICENSE.md",
        }
