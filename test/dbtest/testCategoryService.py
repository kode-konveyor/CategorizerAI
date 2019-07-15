#coding=utf-8
import unittest
from dbtest import ConnectionStubProvider, DbTestHelper
from springboot.Autowired import Autowired

categoryService = Autowired('categoryService')
config = Autowired('config')
class Test(unittest.TestCase):

    def setUp(self):
        self.fakeConnection = ConnectionStubProvider.allStubs()
        self.categories = categoryService.fetchCategories(self.fakeConnection)

    def test_returns_a_dict_keyed_with_the_element_ID_COLUMN_POSITION_IN_CATEGORIES_TABLE(self):
        firstRow = DbTestHelper.all_rows[0]
        firstRowKey = firstRow[config.ID_COLUMN_POSITION_IN_CATEGORIES_TABLE]
        self.assertEqual(
            firstRow,
            self.categories[firstRowKey]
            )

    def test_the_returned_dict_contains_elements_for_all_different_keys(self):
        self.assertEqual(
            len(DbTestHelper.all_rows),
            len(self.categories)
            )

    def test_closes_the_connection(self):
        self.fakeConnection.cursor.assert_called_once()

    def test_executes_SQL_TO_OBTAIN_CATEGORIES(self):
        argsList = self.fakeConnection.cursor.execute.call_args_list
        self.assertEqual(1, len(argsList))
        self.assertEqual(config.SQL_TO_OBTAIN_CATEGORIES, argsList[0][0][0])
