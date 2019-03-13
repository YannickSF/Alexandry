
import json
import requests
import threading
from requests import RequestException
from jsonschema import validate, ValidationError
from blockchain.settings import CONFIG


with open('{0}.json'.format('core/schemas/txion'), encoding='utf-8') as data:
    schema_txion = json.load(data)

with open('{0}.json'.format('core/schemas/block'), encoding='utf-8') as data:
    schema_block = json.load(data)


class Worker:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def validate_block(self):
        pass

    def validate_txion(self):
        pass

    def validate_telegraph(self):
        pass
