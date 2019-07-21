import unittest
from winterboot.Autowired import Autowired
import TestHelper

accuracyErrorDisplayService = Autowired("accuracyErrorDisplayService")

class Test(unittest.TestCase):

    def testdisplayTransaction_prints_the_transaction(self):
        with\
                Autowired('uiTestData', self),\
                unittest.mock.patch('sys.stdout') as mockedStdout:
            accuracyErrorDisplayService().displayAccurracyError()
        TestHelper.assertPrintedOn(mockedStdout, self.uiTestData.ACCURACY_ERROR_MESSAGE)


if __name__ == "__main__":
    unittest.main()