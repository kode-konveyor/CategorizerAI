#coding=utf-8
import unittest
from aitest import AiTestHelper
from springboot.Autowired import Autowired
from springboot.MockedService import MockedService

accuracyCheckService = Autowired('accuracyCheckService')
config = Autowired('config')

class Test(unittest.TestCase):

    def runTestWithAccuracy(self, accuracy):
        with MockedService('displayAccuracyService') as self.displayAccuracyService:
            with MockedService('accuracyErrorDisplayService') as self.accuracyErrorDisplayService:
                with unittest.mock.patch('sys.exit') as self.sysExit:
                    accuracyCheckService.checkAccuracy(accuracy)

    def test_checkAccuracy_displays_accuracy(self):
        self.runTestWithAccuracy(AiTestHelper.ACCURACY)
        callArguments = self.displayAccuracyService.displayAccuracy.call_args_list
        self.assertEqual(AiTestHelper.ACCURACY, callArguments[0][0][0])

    def test_checkAccuracy_exits_when_accuracy_is_low(self):
        self.runTestWithAccuracy(AiTestHelper.LOW_ACCURACY)
        callArguments = self.sysExit.call_args_list
        self.assertEqual(-1, callArguments[0][0][0])

    def test_checkAccuracy_displays_accuracy_error_message_when_accuracy_is_low(self):
        self.runTestWithAccuracy(AiTestHelper.LOW_ACCURACY)
        self.accuracyErrorDisplayService.displayAccurracyError.assert_called_once()

