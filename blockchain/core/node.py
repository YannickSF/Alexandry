
import threading
from .blockchain import Blockchain
from .worker import Worker


class Node:
    def __init__(self):
        self.blockchain = Blockchain()
        self.worker = Worker(self.blockchain)

