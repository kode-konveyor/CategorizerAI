#coding=utf-8
import unittest
from springboot.Autowired import Autowired
from dbtest.DbTestData import DbTestData


connectionFactory = Autowired('connectionFactory')
config = Autowired('config')
class Test(unittest.TestCase):

    def setUp(self):
        dbTestData = DbTestData()
        self.fakeConnection = dbTestData.connection
        with unittest.mock.patch('psycopg2.connect', new = dbTestData.connector) as connector:
            self.connector = connector
            self.connection = connectionFactory.obtainConnection()

    def test_obtainConnection_calls_connect_of_DATABASE_CONNECTOR(self):
        self.assertEqual(self.fakeConnection, self.connection)

    def test_obtainConnection_calls_connect_with_configured_connect_string(self):
        callArguments = self.connector.call_args_list
        self.assertEqual(config.CONNECTION_STRING, callArguments[0][0][0])


if __name__ == "__main__":
    unittest.main()