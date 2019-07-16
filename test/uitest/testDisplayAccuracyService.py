import unittest
from categorizerai.winterboot.Autowired import Autowired
from aitest.AiTestData import AITestData
import TestHelper
from categorizerai.ui import DisplayAccuracyService


displayAccuracyService = Autowired("displayAccuracyService")

class Test(unittest.TestCase):

    def testdisplayTransaction_prints_the_transaction(self):
        aiTestData = AITestData()
        with unittest.mock.patch('sys.stdout') as mockedStdout:
            displayAccuracyService.displayAccuracy(aiTestData.ACCURACY)
        TestHelper.assertPrintedOn(mockedStdout, DisplayAccuracyService.ACCURACY_STRING.format(aiTestData.ACCURACY))


if __name__ == "__main__":
    unittest.main()