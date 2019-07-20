import unittest
from winterboot.Autowired import Autowired
import TestHelper

transactionDisplayService = Autowired("transactionDisplayService")
class Test(unittest.TestCase):

    def testdisplayTransaction_prints_the_transaction(self):
        with\
                Autowired('dbTestData', self),\
                unittest.mock.patch('sys.stdout') as mockedStdout:
            transactionDisplayService().displayTransaction(self.dbTestData.fetched_row)
        TestHelper.assertPrintedOn(mockedStdout, self.dbTestData.fetched_row)


if __name__ == "__main__":
    unittest.main()