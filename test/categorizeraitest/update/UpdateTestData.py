from categorizeraitest.data.DataTestData import DataTestData
from unittest.mock import MagicMock

class UpdateTestData(object):
    def __init__(self):
        self.testData = DataTestData()
        self.data=self.makePreparedData()
        self.data.problemResults = self.testData.PROBLEM_MODEL_INPUT
        self.categories = {
            1: (1, "a", "b"),
            2: (2, "c", "d"),
            3: (3, "e", "f"),
            }
        self.rowNumber = 1
        self.choice = "choice"
        self.oidAsStr = str(self.testData.PROBLEM_OIDS[self.rowNumber])
        self.resultKeys = [1, 2]
        self.PREPARED_OPTIONS = {1: (0.6, (3, 'e', 'f')), 2: (0.3, (1, 'a', 'b'))}
        self.outputOfFirstOption = "\t 1: 0.6 (3, 'e', 'f')"
        self.ANSWER_TO_CHOICE_PROMPT = "42"
    
        self.existingChoice = "1"
        self.nonExistingChoice = "4"
        self.regexConformantChoiceInput = "one,two"
        self.choiceFromRegexConformantInput = self.regexConformantChoiceInput.split(",")

    def makePreparedData(self):
        data = MagicMock()
        data.problemOids = self.testData.PROBLEM_OIDS
        data.problemValues = self.testData.PROBLEM_MODEL_RESULT
        data.output_neurons = self.testData.OUTPUT_NEURONS
        data.max_length = self.testData.MAX_LENGTH
        data.numberOfOutputNeurons = self.testData.OUTPUT_NEURONS
        return data

