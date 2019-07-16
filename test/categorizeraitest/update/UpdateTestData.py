from categorizeraitest.data.DataTestData import DataTestData
from unittest.mock import MagicMock

class UpdateTestData(object):
    testData = DataTestData()
    data = MagicMock()
    data.problemOids = testData.PROBLEM_OIDS
    data.problemValues = testData.PROBLEM_MODEL_RESULT
    data.problemResults = testData.PROBLEM_MODEL_INPUT
    data.output_neurons = testData.OUTPUT_NEURONS
    categories = {
        1: (1, "a", "b"),
        2: (2, "c", "d"),
        3: (3, "e", "f"),
        }
    rowNumber = 1
    choice = "choice"
    oidAsStr = str(testData.PROBLEM_OIDS[rowNumber])
    resultKeys = [1, 2]
    PREPARED_OPTIONS = {1: (0.6, (3, 'e', 'f')), 2: (0.3, (1, 'a', 'b'))}
    outputOfFirstOption = "\t 1: 0.6 (3, 'e', 'f')"
    ANSWER_TO_CHOICE_PROMPT = "42"

    existingChoice = "1"
    nonExistingChoice = "4"
    regexConformantChoiceInput = "one,two"
    choiceFromRegexConformantInput = regexConformantChoiceInput.split(",")

