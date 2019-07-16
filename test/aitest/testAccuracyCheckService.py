#coding=utf-8
import unittest
from categorizerai.winterboot.Autowired import Autowired
from categorizerai.winterboot.MockedService import MockedService
from aitest.AiTestData import AITestData
import TestHelper

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
        TestHelper.assertCallParameter(
            self.aiTestData.ACCURACY,
            self.displayAccuracyService.displayAccuracy, 0)

    def test_checkAccuracy_exits_when_accuracy_is_low(self):
        self.runTestWithAccuracy(self.aiTestData.LOW_ACCURACY)
        TestHelper.assertCallParameter(
            -1,
            self.sysExit, 0)

    def test_checkAccuracy_displays_accuracy_error_message_when_accuracy_is_low(self):
        self.runTestWithAccuracy(self.aiTestData.LOW_ACCURACY)
        self.accuracyErrorDisplayService.displayAccurracyError.assert_called_once()

