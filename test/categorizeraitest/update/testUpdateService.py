import unittest
from winterboot.Autowired import Autowired
from winterboot.MockedService import MockedService
import TestHelper

updateService = Autowired("UpdateService")

class Test(unittest.TestCase):

    def setUp(self):

        with \
          Autowired('UpdateTestData', self),\
          Autowired('DbTestData', self),\
          MockedService('RowUpdateService', self),\
          MockedService('ConnectionService', self),\
          MockedService('CategoryService', self):

            updateService.call(
                self.UpdateTestData.data)

            self.handleOneRowArgs = self.RowUpdateService.call

    def test_handleUpdates_obtains_a_connection(self):
        self.ConnectionService.call.assert_called_once()

    def test_fetches_categories_using_the_connection(self):
        self.CategoryService.call.assert_called_once_with(self.DbTestData.connection)

    def test_calls_RowUpdateService_for_all_rows_in_problem_results(self):
        self.assertEqual(len(self.UpdateTestData.data.problemResults), self.RowUpdateService.call.call_count)


    def test_uses_the_row_number_to_update_rows(self):
        TestHelper.assertFunctionParametersAcrossAllcalls(
            range(len(self.UpdateTestData.data.problemResults)),
            self.handleOneRowArgs,
            0)

if __name__ == "__main__":
    unittest.main()