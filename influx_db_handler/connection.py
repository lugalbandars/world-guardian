from os import getenv

from dotenv import load_dotenv
from influxdb_client import InfluxDBClient

load_dotenv()
token = getenv("indexdb_token")
org = getenv("indexdb_org")
bucket = getenv("indexdb_bucket")

client = InfluxDBClient(url=getenv("indexdb_host"), token=token)
