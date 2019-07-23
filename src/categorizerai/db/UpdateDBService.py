from winterboot.Autowired import Autowired
from winterboot.Service import Service
import types

config = Autowired('Config')()

@Service
class UpdateDBService:
    
    def call(self, connection, oid, row, choice):
        table = config.figureOutTable(row)
        sentence = self._createUpdateSentence(oid, choice, table)
        cursor = connection.cursor()
        cursor.execute(sentence)
        connection.commit()
        cursor.close()

    def _createUpdateSentence(self, oid, choice, table):
        args = types.SimpleNamespace()
        args.table = table
        args.choice = choice
        args.oid = oid
        sentence = config.SQL_TO_UPDATE_RECORD.format(args)
        return sentence

