import unittest
from springboot.Autowired import Autowired
from uitest.UITestBase import UITestBase
from ui import ChoiceAskService

ANSWER_TO_CHOICE_PROMPT = "42"

choiceAskService = Autowired("choiceAskService")
class Test(UITestBase):

    def setUp(self):
        with unittest.mock.patch('sys.stdin') as mockedStdin:
            with unittest.mock.patch('sys.stdout') as self.mockedStdout:
                mockedStdin.readline.return_value = ANSWER_TO_CHOICE_PROMPT
                self.answer = choiceAskService.askUserForChoice()

    def test_askUserForChoice_displays_prompt(self):
        argsList = self.mockedStdout.write.call_args_list
        self.assertEqual(ChoiceAskService.PROMPT, argsList[0][0][0])

    def test_askUserForChoice_returns_value_given_in_stdin(self):
        self.assertEqual(ANSWER_TO_CHOICE_PROMPT, self.answer)


if __name__ == "__main__":
    unittest.main()