from flask_restful import reqparse, inputs

from filters.abstract_filter import AbstractFilter


class MemberFilter(AbstractFilter):
    def filter(self):
        parser = reqparse.RequestParser()
        parser.add_argument('member', type=inputs.boolean, help='[String] Filter for member worlds.')
        args = parser.parse_args()
        member = args['member']

        if member is not None:
            world_list = [world for world in self._world_list if
                          world.type is not None and (world.type == 'members') is member]
            return world_list
        return self._world_list
