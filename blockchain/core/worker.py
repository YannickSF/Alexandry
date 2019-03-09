
import json
import requests
import threading
from requests import RequestException
from jsonschema import validate, ValidationError
from blockchain.settings import CONFIG


with open('{0}.json'.format('core/schemas/txion'), encoding='utf-8') as data:
    schema_txion = json.load(data)

with open('{0}.json'.format('core/schemas/block'), encoding='utf-8') as data:
    schema_block = json.load(data)


class Worker:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.tx_counter = 0

    def _process(self):
        def task():
            if self.tx_counter >= CONFIG.MAX_TX_PER_BLOCK:
                block = self.blockchain.create_block()
                self.validate_block(block)

        task = threading.Thread(target=task)
        task.start()
        task.join()

    """ Block """
    def validate_block(self, block):
        CONFIG.blockchain_logger.info('START VALIDATING BLOCK : ' + block['hash'])
        try:
            validate(block, schema_block)
            CONFIG.blockchain_logger.info('BLOCK VALIDATE : #1 - schema OK - ' + block['hash'])
            block_status = []

            try:
                for node in CONFIG.NODES:
                    CONFIG.blockchain_logger.info('BLOCK VALIDATE : #2 - sending to node : [' + node + '] - ' + block.hash)
                    send = requests.post('http://{0}:{1}{2}'.format(node, CONFIG.PORT, CONFIG.TRX_URI_BLOCK),
                                         data=block)
                    status = send.json()
                    CONFIG.blockchain_logger.info('BLOCK VALIDATE : #2 - sending to node : [' + node + '] - ' + block.hash)
                    block_status.append(status['status'])

                if False not in block_status:
                    CONFIG.blockchain_logger.info('BLOCK VALIDATE : #3 - Certificate : OK - ' + block['hash'])
                else:
                    CONFIG.blockchain_logger.warning('BLOCK VALIDATE : #3 - Certificate : KO - ' + block['hash'])

            except RequestException:
                CONFIG.blockchain_logger.error('ERROR : Joining network.')

        except ValidationError:
            CONFIG.blockchain_logger.warning('WARNING : Invalid Block format.')

        finally:
            CONFIG.blockchain_logger.info('END VALIDATING BLOCK: ' + block['hash'])

    @staticmethod
    def callback_validate_block(block):
        try:
            validate(block, schema_block)
            CONFIG.blockchain_logger.info('CALLBACK - BLOCK : [' + block['hash'] + '] - OK')
            return True

        except ValidationError:
            CONFIG.blockchain_logger.warning('CALLBACK - BLOCK : [' + block['hash'] + '] - KO')
            return False

    """ Txion """
    def validate_txion(self, *tupples):

        hash = ''
        for letter in tupples:
            hash += letter
        result_set = self.blockchain.get_txion_by_hash(hash)
        txion = result_set[0]

        CONFIG.blockchain_logger.info('START VALIDATING TXION: ' + txion['hash'])
        try:
            validate(txion, schema_txion)
            CONFIG.blockchain_logger.info('TXION VALIDATE : #1 - schema OK - ' + txion['hash'])
            txion_status = []

            try:
                for node in CONFIG.NODES:
                    CONFIG.blockchain_logger.info('TXION VALIDATE : #2 - sending to node : [' + node + '] - ' + txion['hash'])
                    send = requests.post('http://{0}:{1}{2}'.format(node, CONFIG.PORT, CONFIG.TRX_URI_TXION),
                                         data=txion)
                    status = send.json()
                    CONFIG.blockchain_logger.info('TXION VALIDATE : #2 - sending to node : [' + node + '] - ' + txion['hash'])
                    txion_status.append(status)

                if False not in txion_status:
                    CONFIG.blockchain_logger.info('TXION VALIDATE : #3 - Certificate : OK - ' + txion['hash'])
                    self.tx_counter += 1
                    self._process()
                else:
                    CONFIG.blockchain_logger.warning('BLOCK VALIDATE : #3 - Certificate : KO - ' + txion['hash'])

            except RequestException:
                CONFIG.blockchain_logger.error('ERROR : Joining network.')

        except ValidationError:
            CONFIG.blockchain_logger.warning('WARNING : Invalid Txion format.')

        finally:
            CONFIG.blockchain_logger.info('END VALIDATING TXION: ' + txion['hash'])

    @staticmethod
    def callback_validate_txion(txion):
        try:
            validate(txion, schema_txion)
            CONFIG.blockchain_logger.info('CALLBACK - TXION : [' + txion['hash'] + '] - KO')
            return True

        except ValidationError:
            CONFIG.blockchain_logger.warning('CALLBACK - TXION : [' + txion['hash'] + '] - KO')
            return False
