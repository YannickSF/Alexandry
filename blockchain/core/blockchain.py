
import datetime
from tinydb import TinyDB, Query
# remove 'Main.' on linux terminal
from blockchain.core.objects.block import Block
from blockchain.core.objects.txion import Txion
from blockchain.core.objects.telegraph import Telegraph
from blockchain.settings import CONFIG


class Blockchain:
    def __init__(self):
        self.blockchain = TinyDB(path=CONFIG.BLOCKCHAIN_PATH, indent=4, default_table=CONFIG.BLOCKCHAIN_NAME)
        self.txion_ledger = TinyDB(path=CONFIG.TXION_PATH, indent=4, default_table='txion')
        self.builder = TinyDB(path=CONFIG.BUILDER_PATH, indent=4, default_table='builder')

    def get_blockchain(self):
        return self.blockchain.all()

    """ Block """
    def create_block(self):
        tmpstp = datetime.datetime.now()

        new_block = Block(CONFIG.block_index(self),
                          CONFIG.convert_builder(self.builder),
                          tmpstp.strftime('%a, %d %b %Y %H:%M:%S'),
                          CONFIG.block_last_hash(self))

        self.blockchain.insert(new_block.__repr__())
        CONFIG.blockchain_logger.info('NEW BLOCK : [' + new_block.hash + ']')
        return new_block

    def get_block_by_hash(self, p_hash):
        QBlock = Query()
        return self.blockchain.search(QBlock.hash == p_hash)

    def get_block_by_id(self, id):
        QBlock = Query()
        return self.blockchain.search(QBlock.index == id)

    def insert_block(self, block):
        self.blockchain.insert(block)

    """ Txion """
    def create_txion(self, expeditor, destinator, amount):
        tmpstp = datetime.datetime.now()
        index = CONFIG.txion_index(self)

        new_txion = Txion(index,
                          expeditor,
                          destinator,
                          amount,
                          tmpstp.strftime('%a, %d %b %Y %H:%M:%S'))

        self.builder.insert(new_txion.__repr__())
        self.txion_ledger.insert(new_txion.__repr__())
        CONFIG.blockchain_logger.info('NEW TXION : [' + new_txion.hash + ']')

        return new_txion.__repr__()

    def get_txion_by_id(self, id):
        QTxion = Query()
        return self.txion_ledger.search(QTxion.index == id)

    def get_txion_by_hash(self, hash):
        QTxion = Query()
        return self.txion_ledger.search(QTxion.hash == hash)

    def insert_txion(self, txion):
        self.txion_ledger.insert(txion)

    """ Telegraph """
    def create_telegraph(self, expeditor, destinator, message):
        tmpstp = datetime.datetime.now()

        new_telegraph = Telegraph(expeditor,
                                  destinator,
                                  message,
                                  tmpstp.strftime('%a, %d %b %Y %H:%M:%S'))

        self.builder.insert(new_telegraph.__repr__())
        CONFIG.blockchain_logger.info('NEW TELEGRAPH : [' + new_telegraph.hash + ']')

        return new_telegraph.__repr__()

    def get_telegraph_by_hash(self, hash):
        QTxion = Query()
        return self.txion_ledger.search(QTxion.hash == hash)

    def insert_telegraph(self, txion):
        self.txion_ledger.insert(txion)

