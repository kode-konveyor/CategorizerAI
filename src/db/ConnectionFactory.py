from springboot.Autowired import Autowired
from springboot.Service import Service

config = Autowired('config')
@Service
class ConnectionFactory(object):
    def obtainConnection(self):
        connection = config.DATABASE_CONNECTOR.connect(config.CONNECTION_STRING)
        return connection

