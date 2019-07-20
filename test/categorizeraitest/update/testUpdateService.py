import unittest
from winterboot.Autowired import Autowired
from winterboot.MockedService import MockedService
import TestHelper

updateService = Autowired("updateService")

class Test(unittest.TestCase):

    def setUp(self):

        with \
          Autowired('updateTestData', self),\
          Autowired('dbTestData', self),\
          MockedService('rowUpdateService', self),\
          MockedService('connectionService', self),\
          MockedService('categoryService', self):

            self.connectionService.obtainConnection.return_value = self.dbTestData.connection
            self.categoryService.fetchCategories.return_value = self.updateTestData.categories

            updateService().handleUpdates(
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