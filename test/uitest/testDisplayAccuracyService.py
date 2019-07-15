import unittest
from springboot.Autowired import Autowired
from uitest.UITestBase import UITestBase
from ui import DisplayAccuracyService
from aitest import AiTestHelper


displayAccuracyService = Autowired("displayAccuracyService")

class Test(UITestBase):

    def testdisplayTransaction_prints_the_transaction(self):
        Autowired.wire()
        with unittest.mock.patch('sys.stdout') as mockedStdout:
            displayAccuracyService.displayAccuracy(AiTestHelper.ACCURACY)
        self.assertPrintedOn(mockedStdout, DisplayAccuracyService.ACCURACY_STRING.format(AiTestHelper.ACCURACY))


if __name__ == "__main__":
    unittest.main()