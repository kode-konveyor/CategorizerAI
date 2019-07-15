#coding=utf-8
import unittest
from springboot.Autowired import Autowired
from dbtest.DbTestData import DbTestData

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
        argsList = self.fakeConnection.cursor.execute.call_args_list
        self.assertEqual(1, len(argsList))
        self.assertEqual(
            self.dbTestData.formattedUpdateQuery,
            argsList[0][0][0])
