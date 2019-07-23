from winterboot.Autowired import Autowired
from winterboot.Service import Service

Config = Autowired('Config')

@Service
class RowProviderService:

    def call(self, connection, oidAsStr):
        cursor = connection.cursor()
        sqlCommand = Config().SQL_TO_OBTAIN_TRANSACTION_BY_OID.format(oidAsStr)
        cursor.execute(sqlCommand)
        row = cursor.fetchone()
        cursor.close()
        return row
