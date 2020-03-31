
import datetime
from .config import CONFIG

from .database import BlockchainDB, UNTxionsDB, TxionsDB, Query
from core.objects.block import Block
from core.objects.txion import Txion


MAX_COIN = 21000000000
REWARD = 25


class Blockchain:
    def __init__(self):
        self._data_to_validate = []

    """ Blockchain """
    @staticmethod
    def get_blockchain():
        return BlockchainDB.all()

    def _block_last_hash(self):
        last_block = self.get_block_by_id(len(BlockchainDB.all()) - 1)
        return last_block.hash

    """ Block """
    def create_block(self):
        tmpstp = datetime.datetime.now()

        new_block = Block(CONFIG.block_index(self),
                          self._data_to_validate,
                          tmpstp.strftime('%a, %d %b %Y %H:%M:%S'),
                          self._block_last_hash())

        BlockchainDB.insert(new_block.__repr__())
        return new_block

    @staticmethod
    def get_block_by_hash(p_hash):
        QBlock = Query()
        return BlockchainDB.find_first(QBlock.hash == p_hash)

    @staticmethod
    def get_block_by_id(id):
        QBlock = Query()
        return BlockchainDB.find_first(QBlock.index == id)

    """ Txion """
    def transfer(self, expeditor, destinator, amount):
        tmpstp = datetime.datetime.now()
        index = CONFIG.txion_index(self)

        new_txion = Txion(index,
                          expeditor,
                          destinator,
                          amount,
                          tmpstp.strftime('%a, %d %b %Y %H:%M:%S'))

        self._data_to_validate.append(new_txion.__repr__())
        UNTxionsDB.insert(new_txion)
        return new_txion.__repr__()

    @staticmethod
    def get_txion_by_id(id):
        # controler UNTxionDB
        QTxion = Query()
        return TxionsDB.insert(QTxion.index == id)

    @staticmethod
    def get_txion_by_hash(hash):
        # controler UNTxionDB
        QTxion = Query()
        return TxionsDB.find_first(QTxion.hash == hash)
