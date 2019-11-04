#coding=utf-8
import unittest
from winterboot.Autowired import Autowired
from winterboot.MockedService import MockedService
import TestHelper

accuracyCheckService = Autowired('AccuracyCheckService')

class Test(unittest.TestCase):

    def setUp(self):
        with Autowired('AiTestData', self, singleton=False):
            pass

    def runTestWithAccuracy(self, accuracy):
        with\
            MockedService('DisplayAccuracyService', self),\
            MockedService('AccuracyErrorDisplayService', self),\
            unittest.mock.patch('sys.exit') as self.sysExit:
                    accuracyCheckService.call(accuracy)

    def test_checkAccuracy_displays_accuracy(self):
        self.runTestWithAccuracy(self.AiTestData.ACCURACY)
        TestHelper.assertCallParameter(
            self.AiTestData.ACCURACY,
            self.DisplayAccuracyService.call, 0)

    def test_checkAccuracy_exits_when_accuracy_is_low(self):
        self.runTestWithAccuracy(self.AiTestData.LOW_ACCURACY)
        TestHelper.assertCallParameter(
            -1,
            self.sysExit, 0)

    def test_checkAccuracy_displays_accuracy_error_message_when_accuracy_is_low(self):
        self.runTestWithAccuracy(self.AiTestData.LOW_ACCURACY)
        self.AccuracyErrorDisplayService.call.assert_called_once()

