
import hashlib


class Txion:
    def __init__(self, index, expeditor, destinator, amount, timestamp, serial=False, hash=''):
        self.index = index
        self.expeditor = expeditor
        self.destinator = destinator
        self.amount = amount
        self.timestamp = timestamp
        self.hash = None

        if serial is False:
            self._bc_format()
        else:
            self.hash = hash

    def _bc_format(self):
        sha = hashlib.sha256()
        payload = {'index': self.index,
                   'expeditor': self.expeditor,
                   'destinator': self.destinator,
                   'amount': self.amount,
                   'timestamp': self.timestamp,
                   'hash': self.hash}

        sha.update(str(payload).encode('utf-8'))

        self.hash = sha.hexdigest()

    def __repr__(self):
        return {'hash': self.hash,
                'index': self.index,
                'expeditor': self.expeditor,
                'destinator': self.destinator,
                'amount': self.amount,
                'timestamp': self.timestamp}

    def __str__(self):
        return self.__repr__().__str__()
