
import hashlib


class Telegraph:
    def __init__(self, expeditor, destinator, message, timestamp, serial=False, hash=''):
        self.expeditor = expeditor
        self.destinator = destinator
        self.message = message
        self.timestamp = timestamp
        self.hash = None

        if serial is False:
            self._bc_format()
        else:
            self.hash = hash

    def _bc_format(self):
        sha = hashlib.sha256()
        payload = {'expeditor': self.expeditor,
                   'destinator': self.destinator,
                   'message': self.message,
                   'timestamp': self.timestamp,
                   'hash': self.hash}

        sha.update(str(payload).encode('utf-8'))

        self.hash = sha.hexdigest()

    def __repr__(self):
        return {'hash': self.hash,
                'expeditor': self.expeditor,
                'destinator': self.destinator,
                'message': self.message,
                'timestamp': self.timestamp}

    def __str__(self):
        return self.__repr__().__str__()
