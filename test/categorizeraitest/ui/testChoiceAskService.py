import unittest
from winterboot.Autowired import Autowired
from winterboot.MockedService import MockedService
import TestHelper

choiceAskService = Autowired("ChoiceAskService")
class Test(unittest.TestCase):

    def setUp(self):
        with\
                Autowired('UiTestData', self),\
                MockedService('categorizerai.ui.ChoiceAskService.input') as self.mockedInput:
            self.answer = choiceAskService.call()

    def test_askUserForChoice_displays_prompt(self):
        TestHelper.assertCallParameter(self.UiTestData.PROMPT, self.mockedInput, 0)

    def test_askUserForChoice_returns_value_given_in_stdin(self):
        self.assertEqual(self.UiTestData.ANSWER_TO_CHOICE_PROMPT, self.answer)


if __name__ == "__main__":
    unittest.main()