from categorizerai.springboot.Autowired import Autowired
from categorizerai.springboot.Service import Service

config = Autowired('config')

@Service
class RowProviderService:

    def getRowByOid(self, connection, oidAsStr):
        cursor = connection.cursor()
        cursor.execute(config.SQL_TO_OBTAIN_TRANSACTION_BY_OID.format(oidAsStr))
        row = cursor.fetchone()
        cursor.close()
        return row
