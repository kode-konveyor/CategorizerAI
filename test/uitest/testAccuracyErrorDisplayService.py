import unittest
from categorizerai.springboot.Autowired import Autowired
import TestHelper
from categorizerai.ui import AccuracyErrorDisplayService

accuracyErrorDisplayService = Autowired("accuracyErrorDisplayService")

class Test(unittest.TestCase):

    def testdisplayTransaction_prints_the_transaction(self):
        with unittest.mock.patch('sys.stdout') as mockedStdout:
            accuracyErrorDisplayService.displayAccurracyError()
        TestHelper.assertPrintedOn(mockedStdout, AccuracyErrorDisplayService.ACCURACY_ERROR_MESSAGE)


if __name__ == "__main__":
    unittest.main()