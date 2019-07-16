#coding=utf-8
import unittest
from categorizerai.springboot.Autowired import Autowired
from dbtest.DbTestData import DbTestData
import TestHelper


connectionService = Autowired('connectionService')
config = Autowired('config')
class Test(unittest.TestCase):

    def setUp(self):
        dbTestData = DbTestData()
        self.fakeConnection = dbTestData.connection
        with unittest.mock.patch('psycopg2.connect', new = dbTestData.connector) as connector:
            self.connector = connector
            self.connection = connectionService.obtainConnection()

    def test_obtainConnection_calls_connect_of_DATABASE_CONNECTOR(self):
        self.assertEqual(self.fakeConnection, self.connection)

    def test_obtainConnection_calls_connect_with_configured_connect_string(self):
        TestHelper.assertCallParameter(config.CONNECTION_STRING, self.connector, 0)

if __name__ == "__main__":
    unittest.main()