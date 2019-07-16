import unittest
from categorizerai.winterboot.Autowired import Autowired
from updatetest.UpdateTestData import UpdateTestData
from uitest import ChoiceObtainerTestStubs
from categorizerai.winterboot.MockedService import MockedService

choiceObtainerService = Autowired('choiceObtainerService')

class Test(unittest.TestCase):


    def setUp(self):
        testData = UpdateTestData()
        self.existingChoice = testData.existingChoice
        self.nonExistingChoice = testData.nonExistingChoice
        self.regexConformantChoiceInput = testData.regexConformantChoiceInput
        self.choiceFromRegexConformantInput = testData.choiceFromRegexConformantInput
        self.regexConformantChoiceInput = testData.regexConformantChoiceInput
        self.regexConformantChoiceInput = testData.regexConformantChoiceInput
        self.options = testData.PREPARED_OPTIONS

    def runTest(self, choice):
        with MockedService('choiceAskService') as choiceAskService:
            ChoiceObtainerTestStubs.choiceObtainerStubs(choice)

            choice = choiceObtainerService.obtainChoice(self.options)
        return choice

    def test_choiceOptionService_returns_the_oid_for_option_corresponding_to_a_number_input(self):
        choice = self.runTest(self.existingChoice)
        self.assertEqual(self.options[1][1], choice)

    def test_choiceOptionService_returns_None_if_there_is_no_choice_corresponding_to_a_number_input(self):
        choice = self.runTest(self.nonExistingChoice)
        self.assertEqual(None, choice)

    def testchoiceOptionService_returns_the_input_split_along_comma_if_it_matches_CHOICE_FORMAT_REGEX(self):
        choice = self.runTest(self.regexConformantChoiceInput)
        self.assertEqual(self.choiceFromRegexConformantInput, choice)

if __name__ == "__main__":
    unittest.main()