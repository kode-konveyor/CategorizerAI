import unittest
from categorizerai.springboot.Autowired import Autowired
from categorizerai.springboot.MockedService import MockedService
from updatetest.UpdateTestData import UpdateTestData
from dbtest.DbTestData import DbTestData
import TestHelper

updateService = Autowired("updateService")

class Test(unittest.TestCase):

    def setUp(self):
        self.updateTestData = UpdateTestData()
        self.dbTestData = DbTestData()

        with \
          MockedService('rowUpdateService') as rowUpdateService,\
          MockedService('connectionService') as connectionService,\
          MockedService('categoryService') as categoryService:
            self.rowUpdateService = rowUpdateService
            self.connectionService = connectionService
            self.categoryService = categoryService

            self.connectionService.obtainConnection.return_value = self.dbTestData.connection
            self.categoryService.fetchCategories.return_value = self.updateTestData.categories

            updateService.handleUpdates(
                self.updateTestData.data)

            self.handleOneRowArgs = self.rowUpdateService.handleOneRow

    def test_handleUpdates_obtains_a_connection(self):
        self.connectionService.obtainConnection.assert_called_once()

    def test_fetches_categories_using_the_connection(self):
        self.categoryService.fetchCategories.assert_called_once_with(self.dbTestData.connection)

    def test_calls_rowUpdateService_for_all_rows_in_problem_results(self):
        self.assertEqual(len(self.updateTestData.data.problemResults), self.rowUpdateService.handleOneRow.call_count)


    def test_uses_the_row_number_to_update_rows(self):
        TestHelper.assertFunctionParametersAcrossAllcalls(
            range(len(self.updateTestData.data.problemResults)),
            self.handleOneRowArgs,
            0)

        

if __name__ == "__main__":
    unittest.main()