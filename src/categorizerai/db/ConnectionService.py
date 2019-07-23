from winterboot.Autowired import Autowired
from winterboot.Service import Service
from urllib.parse import urlparse

config = Autowired('Config')()
@Service
class ConnectionService(object):
    def call(self):
        result = urlparse(config.CONNECTION_STRING)
        return config.DATABASE_CONNECTOR.connect(
            user = result.username,
            password = result.password,
            database = result.path[1:],
            host = result.hostname,
            port = result.port)

