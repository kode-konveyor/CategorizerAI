from winterboot.Autowired import Autowired
from winterboot.Service import Service
from urllib.parse import urlparse
import psycopg2

config = Autowired('Config')()
@Service
class ConnectionService(object):
    def call(self) -> psycopg2.extensions.connection:
        result = urlparse(config.CONNECTION_STRING)
        connection = config.DATABASE_CONNECTOR.connect(
            user = result.username,
            password = result.password,
            database = result.path[1:],
            host = result.hostname,
            port = result.port)
        print (connection.__class__)
        return connection

