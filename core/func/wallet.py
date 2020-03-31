
import json
from core.database import WalletsDB

with open('{0}.json'.format('../../datas/account.json'), encoding='utf-8') as data:
    account = json.load(data)


class Wallet:
    def __init__(self):
        self._private_key = None
        self.public_key = None
        self.balance = 0

    @ staticmethod
    def create():
        tmp = dict()
        # save tmp to account
        pass

    def open(self, pubkey, privkey):
        pass

    def balance(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        return self.__repr__().__str__()
