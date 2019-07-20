import unittest
from winterboot.Autowired import Autowired
from winterboot.MockedService import MockedService
import TestHelper

rowUpdateService = Autowired("rowUpdateService")

class Test(unittest.TestCase):

    def setUp(self):
        with \
          Autowired('dbTestData', self),\
          Autowired('dataTestData', self),\
          Autowired('updateTestData', self):
            self.choice = self.updateTestData.choice

    def runTest(self, choice):
        with \
          MockedService('updateDBService', self),\
          MockedService('rowProviderService', self) as rowProviderService,\
          MockedService('transactionDisplayService', self),\
          MockedService('optionPreparatorService', self),\
          MockedService('choiceObtainerService', self) as choiceObtainerService:
            
            rowProviderService.getRowByOid.return_value = self.dbTestData.fetched_row
            choiceObtainerService.obtainChoice.return_value = choice
            
            rowUpdateService().handleOneRow(
                self.updateTestData.rowNumber,
                self.updateTestData.data,
                self.dbTestData.connection,
                self.updateTestData.categories)

    def test_when_no_choice_given_database_is_not_updated(self):
        self.runTest(None)
        self.updateDBService.updateRow.assert_not_called()

    def test_the_database_row_with_the_the_oid_for_the_row_computed_from_problemoids_is_obtained(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(
            self.updateTestData.oidAsStr,
            self.rowProviderService.getRowByOid, 1)

    def test_the_database_row_is_obtained_through_the_connections(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(
            self.dbTestData.connection,
            self.rowProviderService.getRowByOid, 0)

    def test_the_database_row_is_displayed(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(
            self.dbTestData.fetched_row,
            self.transactionDisplayService.displayTransaction, 0)

    def test_option_preparation_uses_the_row_number(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(
            self.updateTestData.rowNumber,
            self.optionPreparatorService.prepareOptionsToOffer, 0)

    def test_option_preparation_uses_the_data(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(
            self.updateTestData.data,
            self.optionPreparatorService.prepareOptionsToOffer, 1)

    def test_option_preparation_uses_the_categories(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(
            self.updateTestData.categories,
            self.optionPreparatorService.prepareOptionsToOffer, 2)


    def test_the_choice_passed_to_update_is_the_choice_obtained(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(self.choice, self.updateDBService.updateRow, 3)

    def test_the_oid_passed_to_update_is_the_oid_for_the_row(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(
            self.updateTestData.oidAsStr,
            self.updateDBService.updateRow, 1)

    def test_the_database_row_is_updated_through_the_connections(self):
        self.runTest(self.choice)
        TestHelper.assertCallParameter(
            self.dbTestData.connection,
            self.updateDBService.updateRow, 0)
    



if __name__ == "__main__":
    unittest.main()