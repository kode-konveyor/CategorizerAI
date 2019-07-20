import unittest
from winterboot.Autowired import Autowired
import TestHelper
from categorizerai.ui import DisplayAccuracyService


displayAccuracyService = Autowired("displayAccuracyService")

class Test(unittest.TestCase):

    def testdisplayTransaction_prints_the_transaction(self):
        with\
                Autowired('aiTestData',self),\
                unittest.mock.patch('sys.stdout') as mockedStdout:
            displayAccuracyService().displayAccuracy(self.aiTestData.ACCURACY)
        TestHelper.assertPrintedOn(mockedStdout, DisplayAccuracyService.ACCURACY_STRING.format(self.aiTestData.ACCURACY))


if __name__ == "__main__":
    unittest.main()