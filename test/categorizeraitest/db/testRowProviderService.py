#coding=utf-8
import unittest
import re
from winterboot.Autowired import Autowired
import TestHelper

rowProviderService = Autowired('RowProviderService')
class Test(unittest.TestCase):

    def setUp(self):
        with Autowired('DbTestData', self, singleton=False):
            self.fakeConnection = self.DbTestData.connection
            self.row = rowProviderService.call(self.fakeConnection, self.DbTestData.oidAsString)
        
    def test_returns_fetched_row(self):
        self.assertEqual(self.DbTestData.fetched_row, self.row)

    def test_closes_the_connection(self):
        self.fakeConnection.cursor.assert_called_once()

    def test_executes_a_string_containing_the_oid(self):
        self.fakeConnection.cursor.execute.assert_called_once()
        firstArgument = TestHelper.callArgument(self.fakeConnection.cursor.execute, 0)
        self.assertTrue(re.search(self.DbTestData.oidAsString, str(firstArgument)))
