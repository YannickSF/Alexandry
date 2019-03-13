
import os
import logging
from logging import FileHandler, Formatter
from .core.objects.txion import Txion
from .core.objects.block import Block
from .core.objects.telegraph import Telegraph


class AlexandryTest:

    """ MAIN """
    DEBUG = True
    PORT = 7000
    HOST = '0.0.0.0'

    """ LOGS """
    LOGS_PATH = '/core/datas/logs/'

    LOG_FORMAT = '%(asctime)s - %(levelname)s : %(message)s'

    LOG_LEVEL = logging.INFO

    # Blockchain logs
    BLOCKCHAIN_LOGS_PATH = os.path.dirname(__file__) + LOGS_PATH + 'blockchain.log'

    blockchain_logger = logging.getLogger("blockchain")
    blockchain_logger.setLevel(LOG_LEVEL)

    blockchain_logger_file_handler = FileHandler(BLOCKCHAIN_LOGS_PATH)
    blockchain_logger_file_handler.setLevel(LOG_LEVEL)
    blockchain_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
    blockchain_logger.addHandler(blockchain_logger_file_handler)

    """ BLOCKCHAIN """
    BLOCKCHAIN_NAME = 'Alexandry Test'

    CHAIN_PATH = '/core/datas/chain/'

    BUILDER_PATH = os.path.dirname(__file__) + CHAIN_PATH + 'builder_test.json'
    BLOCKCHAIN_PATH = os.path.dirname(__file__) + CHAIN_PATH + 'blockchain_test.json'

    TXION_PATH = os.path.dirname(__file__) + CHAIN_PATH + 'txion_test.json'
    TELEGRAPH_PATH = os.path.dirname(__file__) + CHAIN_PATH + 'telegraph_test.json'

    INITIAL_HASH = 'Hello There, lets start a chain !'
    MAX_TX_PER_BLOCK = 10

    @staticmethod
    def block_index(blockchain):
        return len(blockchain.blockchain.all()) + 1

    @staticmethod
    def txion_index(blockchain):
        return len(blockchain.txion_ledger.all()) + 1

    @staticmethod
    def block_last_hash(blockchain):
        last_block = blockchain.get_block_by_id(len(blockchain.blockchain.all()) - 1)
        return last_block.hash

    @staticmethod
    def convert_db_to_block(item):
        if item is not None:
            return Block(item.index,
                         item.data,
                         item.timestamp,
                         item.last_hash,
                         True, item.hash)

    @staticmethod
    def convert_db_to_txion(item):
        if item is not None:
            return Txion(item.index,
                         item.expeditor,
                         item.destinator,
                         item.amount,
                         item.timestamp,
                         True, item.hash)

    @staticmethod
    def convert_db_to_telegraph(item):
        if item is not None:
            return Telegraph(item.expeditor,
                             item.destinator,
                             item.message,
                             item.timestamp,
                             True, item.hash)

    @staticmethod
    def convert_builder(db_builder):
        retour = []
        if len(db_builder) > 0:
            for item in db_builder:
                retour.append(Txion(item.index,
                                    item.expeditor,
                                    item.destinator,
                                    item.amount,
                                    item.timestamp,
                                    True, item.hash))

        return retour

    """ NETWORK """
    NODES = []

    TRX_URI_BLOCK = '/trx/block'
    TRX_URI_TXION = '/trx/txion'
    TRX_URI_TELEGRAPH = '/trx/telegraph'


# Env Var
CONFIG = AlexandryTest()
