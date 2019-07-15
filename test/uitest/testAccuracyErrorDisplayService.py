import unittest
from springboot.Autowired import Autowired
from uitest.UITestBase import UITestBase
from ui import AccuracyErrorDisplayService

accuracyErrorDisplayService = Autowired("accuracyErrorDisplayService")

class Test(UITestBase):

    def testdisplayTransaction_prints_the_transaction(self):
        Autowired.wire()
        with unittest.mock.patch('sys.stdout') as mockedStdout:
            accuracyErrorDisplayService.displayAccurracyError()
        self.assertPrintedOn(mockedStdout, AccuracyErrorDisplayService.ACCURACY_ERROR_MESSAGE)


if __name__ == "__main__":
    unittest.main()