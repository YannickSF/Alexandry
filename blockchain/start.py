# coding=utf-8

from flask import *
from flask_restful import *
# remove 'Main.' on linux terminal
from blockchain.core.node import Node
from blockchain.settings import CONFIG


app = Flask('__name__')
api = Api(app)
client = Node()


class Blockchain(Resource):
    def get(self):
        return {'{0}'.format(CONFIG.BLOCKCHAIN_NAME): client.blockchain.get_blockchain()}


class Block(Resource):
    def get(self, hash=''):
        if hash != '':
            return {'Block': client.blockchain.get_block_by_hash(hash)}


class Txion(Resource):
    def get(self, hash=''):
        if hash != '':
            return {'Txion': client.blockchain.get_txion_by_hash(hash)}

    def post(self):
        expeditor = request.form['from']
        destinator = request.form['to']
        amount = request.form['amount']

        tx = client.blockchain.create_txion(expeditor, destinator, amount)
        return {'Txion': tx}


class TrxBlock(Resource):
    def post(self):
        block = {}

        if client.worker.callback_validate_block(block):
            client.blockchain.insert_block(block)
            return {'status': True}
        else:
            return {'status': False}


class TrxTxion(Resource):
    def post(self):
        txion = {}

        if client.worker.callback_validate_txion(txion):
            client.blockchain.insert_txion(txion)
            return {'status': True}
        else:
            return {'status': False}


api.add_resource(Blockchain, '/')
api.add_resource(Block, '/block/<string:hash>')
api.add_resource(Txion, '/txion', '/txion/<string:hash>')

api.add_resource(TrxBlock, CONFIG.TRX_URI_BLOCK)
api.add_resource(TrxTxion, CONFIG.TRX_URI_TXION)


if __name__ == '__main__':
    app.run(debug=CONFIG.DEBUG, host=CONFIG.HOST, port=CONFIG.PORT)
