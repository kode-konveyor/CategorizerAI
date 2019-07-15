#coding=utf-8
import unittest
from springboot.Autowired import Autowired
from springboot.MockedService import MockedService
from aitest.AiTestData import AITestData

accuracyCheckService = Autowired('accuracyCheckService')
config = Autowired('config')

class Test(unittest.TestCase):

    def setUp(self):
        self.aiTestData = AITestData()

    def runTestWithAccuracy(self, accuracy):
        with MockedService('displayAccuracyService') as self.displayAccuracyService:
            with MockedService('accuracyErrorDisplayService') as self.accuracyErrorDisplayService:
                with unittest.mock.patch('sys.exit') as self.sysExit:
                    accuracyCheckService.checkAccuracy(accuracy)

    def test_checkAccuracy_displays_accuracy(self):
        self.runTestWithAccuracy(self.aiTestData.ACCURACY)
        callArguments = self.displayAccuracyService.displayAccuracy.call_args_list
        self.assertEqual(self.aiTestData.ACCURACY, callArguments[0][0][0])

    def test_checkAccuracy_exits_when_accuracy_is_low(self):
        self.runTestWithAccuracy(self.aiTestData.LOW_ACCURACY)
        callArguments = self.sysExit.call_args_list
        self.assertEqual(-1, callArguments[0][0][0])

    def test_checkAccuracy_displays_accuracy_error_message_when_accuracy_is_low(self):
        self.runTestWithAccuracy(self.aiTestData.LOW_ACCURACY)
        self.accuracyErrorDisplayService.displayAccurracyError.assert_called_once()

