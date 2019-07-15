#coding=utf-8
import unittest
from dbtest import ConnectionStubProvider, DbTestHelper
import re
from springboot.Autowired import Autowired

rowProviderService = Autowired('rowProviderService')
class Test(unittest.TestCase):

    def setUp(self):
        self.fakeConnection = ConnectionStubProvider.allStubs()
        
    def test_returns_fetched_row(self):
        row = rowProviderService.getRowByOid(self.fakeConnection, DbTestHelper.oidAsString)
        self.assertEqual(DbTestHelper.fetched_row, row)

    def test_closes_the_connection(self):
        rowProviderService.getRowByOid(self.fakeConnection, DbTestHelper.oidAsString)
        self.fakeConnection.cursor.assert_called_once()

    def test_executes_a_string_containing_the_oid(self):
        rowProviderService.getRowByOid(self.fakeConnection, DbTestHelper.oidAsString)
        argsList = self.fakeConnection.cursor.execute.call_args_list
        self.assertEqual(1, len(argsList))
        self.assertTrue(re.search(DbTestHelper.oidAsString, str(argsList[0])))
