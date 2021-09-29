from datetime import datetime

from influxdb_client import Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

from influx_db_handler.connection import client, bucket, org


class WorldDataPopulator:

    def __init__(self):
        self.write_api = client.write_api(write_options=SYNCHRONOUS)

    def populate_world_data(self, worlds: list):
        for world in worlds:
            point = Point("world") \
                .tag("number", world.number) \
                .field("player_count", world.player_count) \
                .field("type", world.type) \
                .time(datetime.utcnow(), WritePrecision.NS)

            self.write_api.write(bucket, org, point)
