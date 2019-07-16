from winterboot.Autowired import Autowired
from winterboot.Service import Service

config = Autowired('config')
@Service
class ConnectionService(object):
    def obtainConnection(self):
        connection = config.DATABASE_CONNECTOR.connect(config.CONNECTION_STRING)
        return connection

