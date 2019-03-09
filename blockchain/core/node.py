
import threading
from .blockchain import Blockchain
from .worker import Worker


class Node:
    def __init__(self):
        self.blockchain = Blockchain()
        self.worker = Worker(self.blockchain)

    def validate_block(self, block):
        task = threading.Thread(target=self.worker.validate_block(block))
        task.start()
        task.join()

    def validate_txion(self, txion_hash):
        task = threading.Thread(target=self.worker.validate_txion, args=txion_hash)
        task.start()
        task.join()
