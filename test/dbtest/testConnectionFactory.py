#coding=utf-8
import unittest
from unittest.mock import MagicMock
from dbtest import ConnectionStubProvider
from springboot.Autowired import Autowired

connectionFactory = Autowired('connectionFactory')
config = Autowired('config')
class Test(unittest.TestCase):

    def setUp(self):
        self.fakeConnection = ConnectionStubProvider.allStubs()
        config.DATABASE_CONNECTOR = MagicMock()
        config.DATABASE_CONNECTOR.connect = MagicMock(return_value=self.fakeConnection)
        self.connection = connectionFactory.obtainConnection()

    def test_obtainConnection_calls_connect_of_DATABASE_CONNECTOR(self):
        self.assertEqual(self.fakeConnection, self.connection)

    def test_obtainConnection_calls_connect_with_configured_connect_string(self):
        callArguments = config.DATABASE_CONNECTOR.connect.call_args_list
        self.assertEqual(config.CONNECTION_STRING, callArguments[0][0][0])


if __name__ == "__main__":
    unittest.main()