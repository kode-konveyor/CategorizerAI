#coding=utf-8
import unittest
from categorizerai.winterboot.Autowired import Autowired
from dbtest.DbTestData import DbTestData
import TestHelper

updateDBService = Autowired('updateDBService')
config = Autowired('config')

class Test(unittest.TestCase):

    def setUp(self):
        self.dbTestData = DbTestData()
        self.fakeConnection = self.dbTestData.connection
        updateDBService.updateRow(
            self.fakeConnection,
            self.dbTestData.oidAsString,
            self.dbTestData.fetched_row,
            self.dbTestData.choice)
        
    def test_closes_the_connection(self):
        self.fakeConnection.cursor.assert_called_once()

    def test_executes_the_formatted_update_query(self):
        TestHelper.assertCallParameter(self.dbTestData.formattedUpdateQuery, self.fakeConnection.cursor.execute, 0)
        self.fakeConnection.cursor.execute.assert_called_once()
