import unittest
from springboot.Autowired import Autowired
from uitest.UITestBase import UITestBase
from dbtest.DbTestData import DbTestData

transactionDisplayService = Autowired("transactionDisplayService")
class Test(UITestBase):

    def testdisplayTransaction_prints_the_transaction(self):
        dbTestData = DbTestData()
        Autowired.wire()
        with unittest.mock.patch('sys.stdout') as mockedStdout:
            transactionDisplayService.displayTransaction(dbTestData.fetched_row)
        self.assertPrintedOn(mockedStdout, dbTestData.fetched_row)


if __name__ == "__main__":
    unittest.main()