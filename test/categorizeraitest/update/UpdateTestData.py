from unittest.mock import MagicMock
from winterboot.TestData import TestData
from winterboot.TestDataForStub import TestDataForStub

@TestData
class UpdateTestData(object):
    def __init__(self):
        with TestDataForStub('DataTestData', self):
            self.data=self._makePreparedData()
            self.data.problemResults = self.DataTestData.PROBLEM_MODEL_RESULT
            self.categories = {
                1: (1, "a", "b"),
                2: (2, "c", "d"),
                3: (3, "e", "f"),
                }
            self.rowNumber = 1
            self.choice = "choice"
            self.oidAsStr = str(self.DataTestData.PROBLEM_OIDS[self.rowNumber])
            self.resultKeys = [1, 2]
            self.PREPARED_OPTIONS = {1: (0.6, (3, 'e', 'f')), 2: (0.3, (1, 'a', 'b'))}
            self.outputOfFirstOption = "\t 1: 0.6 (3, 'e', 'f')"
        
            self.existingChoice = "1"
            self.nonExistingChoice = "4"
            self.regexConformantChoiceInput = "one,two"
            self.choiceFromRegexConformantInput = self.regexConformantChoiceInput.split(",")

    def _makePreparedData(self):
        data = MagicMock()
        data.problemOids = self.DataTestData.PROBLEM_OIDS
        data.problemValues = self.DataTestData.PROBLEM_MODEL_RESULT
        data.numberOfOutputNeurons = self.DataTestData.OUTPUT_NEURONS
        data.max_length = self.DataTestData.MAX_LENGTH
        return data

