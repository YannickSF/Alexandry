
from blockchain.blockchain import REWARD
from blockchain.libs.database import BlockchainDB


class Miner:

    def reward(self):
        # send REWARD to self Node
        pass

    @staticmethod
    def coinbase():
        bc = BlockchainDB.all()
        circulate = len(bc) * REWARD
        return circulate

    def mine(self):
        # do pow
        pass
