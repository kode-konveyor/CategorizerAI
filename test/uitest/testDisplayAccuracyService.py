import unittest
from springboot.Autowired import Autowired
from uitest.UITestBase import UITestBase
from ui import DisplayAccuracyService
from aitest.AiTestData import AITestData


displayAccuracyService = Autowired("displayAccuracyService")

class Test(UITestBase):

    def testdisplayTransaction_prints_the_transaction(self):
        aiTestData = AITestData()
        Autowired.wire()
        with unittest.mock.patch('sys.stdout') as mockedStdout:
            displayAccuracyService.displayAccuracy(aiTestData.ACCURACY)
        self.assertPrintedOn(mockedStdout, DisplayAccuracyService.ACCURACY_STRING.format(aiTestData.ACCURACY))


if __name__ == "__main__":
    unittest.main()