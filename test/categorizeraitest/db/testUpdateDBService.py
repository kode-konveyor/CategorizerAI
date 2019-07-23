#coding=utf-8
import unittest
from winterboot.Autowired import Autowired
import TestHelper

updateDBService = Autowired('UpdateDBService')

class Test(unittest.TestCase):

    def setUp(self):
        with Autowired('DbTestData', self, singleton=False):
            self.fakeConnection = self.DbTestData.connection
            updateDBService.call(
                self.fakeConnection,
                self.DbTestData.oidAsString,
                self.DbTestData.fetched_row,
                self.DbTestData.choice)
        
    def test_closes_the_connection(self):
        self.fakeConnection.cursor.assert_called_once()

    def test_executes_the_formatted_update_query(self):
        TestHelper.assertCallParameter(self.DbTestData.formattedUpdateQuery, self.fakeConnection.cursor.execute, 0)
        self.fakeConnection.cursor.execute.assert_called_once()
