
from blockchain.blockchain import Blockchain
from blockchain.core.wallet import Wallet
from blockchain.core.miner import Miner

from blockchain.libs.hmrsa import generate_keypair


class Node:
    pass


def main():
    x, y = generate_keypair(3, 13)
    print(x, y)


if __name__ == '__main__':
    main()
