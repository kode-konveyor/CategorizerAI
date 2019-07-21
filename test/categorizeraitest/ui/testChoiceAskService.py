import unittest
from winterboot.Autowired import Autowired
from winterboot.MockedService import MockedService
import TestHelper

choiceAskService = Autowired("choiceAskService")
class Test(unittest.TestCase):

    def setUp(self):
        with\
                Autowired('uiTestData', self),\
                MockedService('categorizerai.ui.ChoiceAskService.input') as self.mockedInput:
            self.answer = choiceAskService().askUserForChoice()

    def test_askUserForChoice_displays_prompt(self):
        TestHelper.assertCallParameter(self.uiTestData.PROMPT, self.mockedInput, 0)

    def test_askUserForChoice_returns_value_given_in_stdin(self):
        self.assertEqual(self.uiTestData.ANSWER_TO_CHOICE_PROMPT, self.answer)


if __name__ == "__main__":
    unittest.main()