
import datetime

from blockchain.libs.database import TxionsDB
from blockchain.objects.txion import Txion
from blockchain.blockchain import Blockchain


class Wallet:
    def __init__(self):
        self.address = None
        self._private_key = None
        self.public_key = None

    @ staticmethod
    def create():
        pass

    def open(self, pubkey, privkey):
        pass

    def balance(self):
        balance = 0
        dtxs, etxs = Blockchain.get_txion_by_account(self.address)

        for i in range(len(dtxs)):
            balance += dtxs[i]['amount']
        for j in range(len(etxs)):
            balance += etxs[j]['amount']

        return balance

    def send(self, to, amount):
        tmpstp = datetime.datetime.now()
        nounce = None

        # calcul nounce
        new_txion = Txion(index=len(TxionsDB.all()),
                          expeditor=self.public_key,
                          destinator=to,
                          amount=amount,
                          nounce=nounce,
                          timestamp=tmpstp.strftime('%a, %d %b %Y %H:%M:%S'))

        return Blockchain.transfer(new_txion)

    def __repr__(self):
        return {'address': self.address,
                'private': self._private_key,
                'public': self.public_key,
                'balance': self.balance()}

    def __str__(self):
        return self.__repr__().__str__()
