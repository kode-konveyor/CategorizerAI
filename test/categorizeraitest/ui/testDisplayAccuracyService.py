import unittest
from winterboot.Autowired import Autowired
import TestHelper

displayAccuracyService = Autowired("DisplayAccuracyService")

class Test(unittest.TestCase):

    def testdisplayTransaction_prints_the_transaction(self):
        with\
                Autowired('UiTestData',self),\
                Autowired('AiTestData',self),\
                unittest.mock.patch('sys.stdout') as mockedStdout:
            displayAccuracyService.call(self.AiTestData.ACCURACY)
        TestHelper.assertPrintedOn(mockedStdout, self.UiTestData.ACCURACY_STRING.format(self.AiTestData.ACCURACY))


if __name__ == "__main__":
    unittest.main()