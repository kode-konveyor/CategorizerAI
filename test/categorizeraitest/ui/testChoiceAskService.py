import unittest
from winterboot.Autowired import Autowired
import TestHelper
from categorizerai.ui import ChoiceAskService

choiceAskService = Autowired("choiceAskService")
class Test(unittest.TestCase):

    def setUp(self):
        with\
            Autowired('updateTestData', self),\
            unittest.mock.patch('sys.stdin') as mockedStdin,\
            unittest.mock.patch('sys.stdout') as self.mockedStdout:
                mockedStdin.readline.return_value = self.updateTestData.ANSWER_TO_CHOICE_PROMPT
                self.answer = choiceAskService().askUserForChoice()

    def test_askUserForChoice_displays_prompt(self):
        TestHelper.assertCallParameter(ChoiceAskService.PROMPT, self.mockedStdout.write, 0)

    def test_askUserForChoice_returns_value_given_in_stdin(self):
        self.assertEqual(self.updateTestData.ANSWER_TO_CHOICE_PROMPT, self.answer)


if __name__ == "__main__":
    unittest.main()