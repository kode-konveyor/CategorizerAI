import unittest
from categorizerai.winterboot.Autowired import Autowired
from dbtest.DbTestData import DbTestData
import TestHelper

transactionDisplayService = Autowired("transactionDisplayService")
class Test(unittest.TestCase):

    def testdisplayTransaction_prints_the_transaction(self):
        dbTestData = DbTestData()
        with unittest.mock.patch('sys.stdout') as mockedStdout:
            transactionDisplayService.displayTransaction(dbTestData.fetched_row)
        TestHelper.assertPrintedOn(mockedStdout, dbTestData.fetched_row)


if __name__ == "__main__":
    unittest.main()