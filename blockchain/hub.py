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
        expeditor = request.form['expeditor']
        destinator = request.form['destinator']
        amount = request.form['amount']

        tx = client.blockchain.create_txion(expeditor, destinator, amount)
        return {'Txion': tx}


class Telegraph(Resource):
    def get(self, hash=''):
        if hash != '':
            return {'Telegraph': client.blockchain.get_telegraph_by_hash(hash)}

    def post(self):
        expeditor = request.form['expeditor']
        destinator = request.form['destinator']
        message = request.form['message']

        tlgrph = client.blockchain.create_telegraph(expeditor, destinator, message)
        return {'Telegraph': tlgrph}


class TrxBlock(Resource):
    def post(self):
        pass


class TrxTxion(Resource):
    def post(self):
        pass


class TrxTelegraph(Resource):
    def post(self):
        pass


api.add_resource(Blockchain, '/')
api.add_resource(Block, '/block/<string:hash>')
api.add_resource(Txion, '/txion', '/txion/<string:hash>')
api.add_resource(Telegraph, '/telegraph', '/telegraph/<string:hash>')

api.add_resource(TrxBlock, CONFIG.TRX_URI_BLOCK)
api.add_resource(TrxTxion, CONFIG.TRX_URI_TXION)
api.add_resource(TrxTelegraph, CONFIG.TRX_URI_TELEGRAPH)


if __name__ == '__main__':
    app.run(debug=CONFIG.DEBUG, host=CONFIG.HOST, port=CONFIG.PORT)
