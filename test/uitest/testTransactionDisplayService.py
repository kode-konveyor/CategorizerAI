import unittest
from springboot.Autowired import Autowired
from dbtest import DbTestHelper
from uitest.UITestBase import UITestBase

transactionDisplayService = Autowired("transactionDisplayService")
class Test(UITestBase):

    def testdisplayTransaction_prints_the_transaction(self):
        Autowired.wire()
        with unittest.mock.patch('sys.stdout') as mockedStdout:
            transactionDisplayService.displayTransaction(DbTestHelper.fetched_row)
        self.assertPrintedOn(mockedStdout, DbTestHelper.fetched_row)


if __name__ == "__main__":
    unittest.main()