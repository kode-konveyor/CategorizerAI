#coding=utf-8
import unittest
from winterboot.Autowired import Autowired
import TestHelper

updateDBService = Autowired('updateDBService')

class Test(unittest.TestCase):

    def setUp(self):
        with Autowired('dbTestData', self, singleton=False):
            self.fakeConnection = self.dbTestData.connection
            updateDBService().updateRow(
                self.fakeConnection,
                self.dbTestData.oidAsString,
                self.dbTestData.fetched_row,
                self.dbTestData.choice)
        
    def test_closes_the_connection(self):
        self.fakeConnection.cursor.assert_called_once()

    def test_executes_the_formatted_update_query(self):
        TestHelper.assertCallParameter(self.dbTestData.formattedUpdateQuery, self.fakeConnection.cursor.execute, 0)
        self.fakeConnection.cursor.execute.assert_called_once()
