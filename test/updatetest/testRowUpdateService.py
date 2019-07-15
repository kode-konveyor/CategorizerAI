import unittest
from springboot.Autowired import Autowired
from unittest.mock import MagicMock
from springboot.MockedService import MockedService
from datatest.DataTestData import DataTestData
from dbtest.DbTestData import DbTestData
from updatetest.UpdateTestData import UpdateTestData

rowUpdateService = Autowired("rowUpdateService")

class Test(unittest.TestCase):


    def setUp(self):
        self.dbTestData = DbTestData()
        self.testData = DataTestData()
        self.updateTestData = UpdateTestData()
        self.choice = self.updateTestData.choice

    def runTest(self, choice):
        with \
          MockedService('updateDBService') as updateDBService,\
          MockedService('rowProviderService') as rowProviderService,\
          MockedService('transactionDisplayService') as transactionDisplayService,\
          MockedService('optionPreparatorService') as optionPreparatorService,\
          MockedService('choiceObtainerService') as choiceObtainerService:
            self.updateRow = updateDBService.updateRow
            self.getRowByOid = rowProviderService.getRowByOid
            self.displayTransaction = transactionDisplayService.displayTransaction
            self.prepareOptionsToOffer = optionPreparatorService.prepareOptionsToOffer
            
            self.getRowByOid.return_value = self.dbTestData.fetched_row
            choiceObtainerService.obtainChoice.return_value = choice
            
            rowUpdateService.handleOneRow(
                self.updateTestData.rowNumber,
                self.updateTestData.data,
                self.dbTestData.connection,
                self.updateTestData.categories)

    def test_when_no_choice_given_database_is_not_updated(self):
        self.runTest(None)
        self.updateRow.assert_not_called()

    def assertCallParameter(self, expected, functionMock, argPosition, callNumber=0):
        updateRowArgs = functionMock.call_args_list[callNumber][callNumber]
        self.assertEqual(expected, updateRowArgs[argPosition])

    def test_the_choice_passed_to_update_is_the_choice_given(self):
        self.runTest(self.choice)
        self.assertCallParameter(self.choice, self.updateRow, 3)

    def test_the_oid_passed_to_update_is_the_oid_for_the_row(self):
        self.runTest(self.choice)
        self.assertCallParameter(
            self.updateTestData.oidAsStr,
            self.updateRow, 2)

    def test_the_database_row_is_updated_through_the_connections(self):
        self.runTest(self.choice)
        self.assertCallParameter(
            self.dbTestData.connection,
            self.updateRow, 0)
    
    def test_the_database_row_with_the_oid_is_obtained(self):
        self.runTest(self.choice)
        self.assertCallParameter(
            self.updateTestData.oidAsStr,
            self.getRowByOid, 1)

    def test_the_database_row_is_obtained_throug_the_connections(self):
        self.runTest(self.choice)
        self.assertCallParameter(
            self.dbTestData.connection,
            self.getRowByOid, 0)

    def test_the_database_row_is_displayed(self):
        self.runTest(self.choice)
        self.assertCallParameter(
            self.dbTestData.fetched_row,
            self.displayTransaction, 0)

    def test_option_preparation_uses_the_row_number(self):
        self.runTest(self.choice)
        self.assertCallParameter(
            self.updateTestData.rowNumber,
            self.prepareOptionsToOffer, 0)

    def test_option_preparation_uses_the_data(self):
        self.runTest(self.choice)
        self.assertCallParameter(
            self.updateTestData.data,
            self.prepareOptionsToOffer, 1)

    def test_option_preparation_uses_the_categories(self):
        self.runTest(self.choice)
        self.assertCallParameter(
            self.updateTestData.categories,
            self.prepareOptionsToOffer, 2)


if __name__ == "__main__":
    unittest.main()