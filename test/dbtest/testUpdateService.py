#coding=utf-8
import unittest
from dbtest import ConnectionStubProvider, DbTestHelper
from springboot.Autowired import Autowired

updateService = Autowired('updateService')
config = Autowired('config')

class Test(unittest.TestCase):

    def setUp(self):
        self.fakeConnection = ConnectionStubProvider.allStubs()
        updateService.updateRow(
            self.fakeConnection,
            DbTestHelper.oidAsString,
            DbTestHelper.fetched_row,
            DbTestHelper.choice)
        
    def test_closes_the_connection(self):
        self.fakeConnection.cursor.assert_called_once()

    def test_executes_the_formatted_update_query(self):
        argsList = self.fakeConnection.cursor.execute.call_args_list
        self.assertEqual(1, len(argsList))
        self.assertEquals(
            DbTestHelper.formattedUpdateQuery,
            argsList[0][0][0])
