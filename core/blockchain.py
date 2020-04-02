
import datetime
from .config import CONFIG, Singleton

from .database import BlockchainDB, UNTxionsDB, TxionsDB, Query

from core.objects.block import Block


MAX_COIN = 21000000000
REWARD = 100


class Blockchain:
    def __init__(self, metaclass=Singleton):
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
                          UNTxionsDB.all(),
                          tmpstp.strftime('%a, %d %b %Y %H:%M:%S'),
                          self._block_last_hash())

        BlockchainDB.insert(new_block.__repr__())
        UNTxionsDB.purge()
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
    @staticmethod
    def transfer(txion):
        # validate txion
        UNTxionsDB.insert(txion)
        return txion.__repr__()

    @staticmethod
    def get_txion_by_id(id):
        QTxion = Query()
        tx = TxionsDB.insert(QTxion.index == id)
        if tx is None:
            return UNTxionsDB.insert(QTxion.index == id)
        return tx

    @staticmethod
    def get_txion_by_hash(hash):
        QTxion = Query()
        tx = TxionsDB.find_first(QTxion.hash == hash)
        if tx is None:
            return UNTxionsDB.find_first(QTxion.hash == hash)
        return tx

    @staticmethod
    def get_txion_by_account(address):
        QTxion = Query()
        dtxs = TxionsDB.find(QTxion.destinator == address)
        edts = TxionsDB.find(QTxion.expeditor == address)

        un_dtxs = UNTxionsDB.find(QTxion.destinator == address)
        un_edts = UNTxionsDB.find(QTxion.expeditor == address)

        return dtxs + un_dtxs, edts + un_edts