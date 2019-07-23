import unittest
from winterboot.Autowired import Autowired
import TestHelper
from winterboot.MockedService import MockedService

transactionDisplayService = Autowired("TransactionDisplayService")
class Test(unittest.TestCase):

    def testdisplayTransaction_prints_the_transaction(self):
        with\
                Autowired('DbTestData', self),\
                MockedService('sys.stdout') as mockedStdout:
            transactionDisplayService.call(self.DbTestData.fetched_row)
        TestHelper.assertPrintedOn(mockedStdout, self.DbTestData.fetched_row)


if __name__ == "__main__":
    unittest.main()