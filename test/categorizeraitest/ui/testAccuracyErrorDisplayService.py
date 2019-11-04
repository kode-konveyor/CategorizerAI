import unittest
from winterboot.Autowired import Autowired
import TestHelper
from winterboot.MockedService import MockedService

accuracyErrorDisplayService = Autowired("AccuracyErrorDisplayService")

class Test(unittest.TestCase):

    def it_displays_the_transaction(self):
        with\
                Autowired('UiTestData', self),\
                MockedService('sys.stdout') as mockedStdout:
            accuracyErrorDisplayService.displayAccurracyError()
        TestHelper.assertPrintedOn(mockedStdout, self.UiTestData.ACCURACY_ERROR_MESSAGE)


if __name__ == "__main__":
    unittest.main()