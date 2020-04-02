
import os
from tinydb import TinyDB, Query


# Pour fonctionner créer un répertoire 'datas'.
def _data_path(table_name):
    return os.path.dirname(__file__) + '/../datas/{0}.json'.format(table_name)


class _Table:
    """ Class d'accès à la table de donnée
        @table_name : string
    """
    def __init__(self, table_name):
        self._db = TinyDB(path=_data_path(table_name),
                          default_table=table_name, sort_keys=True, indent=4, separators=(',', ': '))
        self._table_length = len(self._db.all())

    """vide la table"""
    def purge(self):
        self._db.purge()

    """ajouter un objet à la table"""
    def insert(self, obj):
        self._db.insert(obj)

    def insert_obj(self, obj):
        self._db.insert(obj.__repr__())

    """ mise à jour d'un objet en base 
    @value : dict{key: value} to update
    @expression : QueryObject comparission
    """
    def update(self, value, expression):
        self._db.update(value, expression)

    """ mise à jour d'un objet en base si l'objet n'existe pas, c'est un insert 
    @value : dict{key: value} to update
    @expression : QueryObject comparission
        """
    def upsert(self, value, expression):
        self._db.upsert(value, expression)
    """ suppression d'une entrée en base"""
    def remove(self, expresion):
        self._db.remove(expresion)

    """ Cherche un/des objets selon le filtre
    @expression : Query Object Expression
    """
    def find(self, expression):
        res = self._db.search(expression)
        if len(res) > 0:
            return res[0]
        return None

    def find_first(self, expression):
        res = self._db.search(expression)
        if len(res) > 0:
            return res[0]
        return None

    """ retourne la list des éléments d'un champ
    @expression : objet Query 
    @ field_name : string : name of the filtre to get"""
    def get_field_data(self, expression, field_name):
        result = [r[field_name] for r in self._db.search(expression)]
        return result

    """Renvoie toutes les entrées de la table"""
    def all(self):
        return self._db.all()


BlockchainDB = _Table('blockchain')
WalletsDB = _Table('wallets')
TxionsDB = _Table('txions')
UNTxionsDB = _Table('untxions')

