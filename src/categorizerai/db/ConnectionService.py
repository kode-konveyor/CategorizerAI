from categorizerai.springboot.Autowired import Autowired
from categorizerai.springboot.Service import Service

config = Autowired('config')
@Service
class ConnectionService(object):
    def obtainConnection(self):
        connection = config.DATABASE_CONNECTOR.connect(config.CONNECTION_STRING)
        return connection

