#coding=utf-8
import unittest
import re
from springboot.Autowired import Autowired
from dbtest.DbTestData import DbTestData

rowProviderService = Autowired('rowProviderService')
class Test(unittest.TestCase):

    def setUp(self):
        self.dbTestData = DbTestData()
        self.fakeConnection = self.dbTestData.connection
        
    def test_returns_fetched_row(self):
        row = rowProviderService.getRowByOid(self.fakeConnection, self.dbTestData.oidAsString)
        self.assertEqual(self.dbTestData.fetched_row, row)

    def test_closes_the_connection(self):
        rowProviderService.getRowByOid(self.fakeConnection, self.dbTestData.oidAsString)
        self.fakeConnection.cursor.assert_called_once()

    def test_executes_a_string_containing_the_oid(self):
        rowProviderService.getRowByOid(self.fakeConnection, self.dbTestData.oidAsString)
        argsList = self.fakeConnection.cursor.execute.call_args_list
        self.assertEqual(1, len(argsList))
        self.assertTrue(re.search(self.dbTestData.oidAsString, str(argsList[0])))
