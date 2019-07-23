import unittest
from winterboot.Autowired import Autowired
from winterboot.MockedService import MockedService
import TestHelper

rowUpdateService = Autowired("RowUpdateService")

class Test(unittest.TestCase):

    def setUp(self):
        with \
          Autowired('DbTestData', self),\
          Autowired('DataTestData', self),\
          Autowired('UpdateTestData', self):
            self.choice = self.UpdateTestData.choice

    def runTest(self, choice):
        with \
          MockedService('UpdateDBService', self),\
          MockedService('RowProviderService', self),\
          MockedService('TransactionDisplayService', self),\
          MockedService('OptionPreparatorService', self),\
          MockedService('ChoiceObtainerService', self):
            
            self.ChoiceObtainerStubs.answerIs(choice)
            
            rowUpdateService.call(
                self.UpdateTestData.rowNumber,
                self.UpdateTestData.data,
                self.DbTestData.connection,
                self.UpdateTestData.categories)

    def test_when_no_choice_given_database_is_not_updated(self):
        self.runTest(None)
        self.UpdateDBService.updateRow.assert_not_called()

    def test_the_database_row_with_the_the_oid_for_the_row_computed_from_problemoids_is_obtained(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(
            self.UpdateTestData.oidAsStr,
            self.RowProviderService.call, 1)

    def test_the_database_row_is_obtained_through_the_connections(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(
            self.DbTestData.connection,
            self.RowProviderService.call, 0)

    def test_the_database_row_is_displayed(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(
            self.DbTestData.fetched_row,
            self.TransactionDisplayService.call, 0)

    def test_option_preparation_uses_the_row_number(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(
            self.UpdateTestData.rowNumber,
            self.OptionPreparatorService.call, 0)

    def test_option_preparation_uses_the_data(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(
            self.UpdateTestData.data,
            self.OptionPreparatorService.call, 1)

    def test_option_preparation_uses_the_categories(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(
            self.UpdateTestData.categories,
            self.OptionPreparatorService.call, 2)


    def test_the_choice_passed_to_update_is_the_choice_obtained(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(self.choice, self.UpdateDBService.call, 3)

    def test_the_oid_passed_to_update_is_the_oid_for_the_row(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(
            self.UpdateTestData.oidAsStr,
            self.UpdateDBService.call, 1)

    def test_the_database_row_is_updated_through_the_connections(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(
            self.DbTestData.connection,
            self.UpdateDBService.call, 0)
    



if __name__ == "__main__":
    unittest.main()