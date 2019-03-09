
import hashlib


class Block:
    def __init__(self, index=None, data=None, timestamp=None, last_hash=None, serial=False, hash=''):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = None

        if serial is False:
            self._bc_format()
        else:
            self.hash = hash

    def _bc_format(self):
        sha = hashlib.sha256()
        payload = {'index': '{0}'.format(self.index),
                   'data': '{0}'.format(self.data),
                   'timestamp': '{0}'.format(self.timestamp),
                   'last_hash': '{0}'.format(self.last_hash)}

        sha.update(str(payload).encode('utf-8'))

        self.hash = sha.hexdigest()

    def __repr__(self):
        return {'hash': self.hash,
                'index': self.index,
                'data': self.data,
                'timestamp': self.timestamp,
                'last_hash': self.last_hash}

    def __str__(self):
        return self.__repr__().__str__()

