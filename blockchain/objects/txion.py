
import hashlib


class Txion:
    def __init__(self, index, expeditor, destinator, amount, timestamp, nounce=None, phash=None):
        self.index = index
        self.expeditor = expeditor
        self.destinator = destinator
        self.amount = amount
        self.timestamp = timestamp
        self.nounce = nounce
        self.hash = phash

    def _bc_format(self):
        sha = hashlib.sha256()
        payload = {'index': self.index,
                   'expeditor': self.expeditor,
                   'destinator': self.destinator,
                   'amount': self.amount,
                   'timestamp': self.timestamp,
                   'nounce': self.nounce,
                   'hash': self.hash}

        sha.update(str(payload).encode('utf-8'))

        self.hash = sha.hexdigest()

    def __repr__(self):
        return {'index': self.index,
                'expeditor': self.expeditor,
                'destinator': self.destinator,
                'amount': self.amount,
                'timestamp': self.timestamp,
                'nounce': self.nounce,
                'hash': self.hash}

    def __str__(self):
        return self.__repr__().__str__()
