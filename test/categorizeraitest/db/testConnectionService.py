#coding=utf-8
import unittest
from winterboot.Autowired import Autowired
import TestHelper

connectionService = Autowired('ConnectionService')
class Test(unittest.TestCase):

    def setUp(self):
        with \
                Autowired('DbTestData', self),\
                unittest.mock.patch('psycopg2.connect', new = self.DbTestData.connector) as connector:
            self.fakeConnection = self.DbTestData.connection
            self.connector = connector
            self.connection = connectionService.call()

    def test_obtainConnection_calls_connect_of_DATABASE_CONNECTOR(self):
        self.assertEqual(self.fakeConnection, self.connection)

    def test_obtainConnection_calls_connect_with_configured_connect_string(self):
        self.assertEqual(self.DbTestData.connectKwArgs, TestHelper.callKwArgument(self.connector))

if __name__ == "__main__":
    unittest.main()