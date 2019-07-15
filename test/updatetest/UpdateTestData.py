from datatest.DataTestData import DataTestData
from unittest.mock import MagicMock

class UpdateTestData(object):
        testData = DataTestData()
        data = MagicMock()
        data.problemOids = testData.PROBLEM_OIDS
        #data.output_neurons = testData.OUTPUT_NEURONS
        #data.problemValues = testData.PROBLEM_MODEL_RESULT
        categories = {}
        rowNumber = 1
        choice = "choice"
        oidAsStr = str(testData.PROBLEM_OIDS[rowNumber])
