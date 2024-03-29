import types
from winterboot.Autowired import Autowired
from winterboot.Service import Service
import pandas
from categorizerai.ai.AIData import AIData

config = Autowired('Config')()
numericConverterService = Autowired('NumericConverterService')

@Service
class PrepareDataService:

    def call(self, trainSet:pandas.DataFrame, problemSet: pandas.DataFrame) -> AIData:
        result = types.SimpleNamespace()
        result.max_length = self._calculateMaximumStringLength(trainSet, problemSet)
        result.numberOfOutputNeurons = max(trainSet.loc[:, config.TRAINING_SET_OUTPUT_COLUMN])+1
    
        result.trainValues = numericConverterService.call(
            trainSet.loc[:, config.PROBLEM_SET_INPUT_COLUMN].values,
            result.max_length)
        result.trainResults = trainSet.loc[:, config.TRAINING_SET_OUTPUT_COLUMN].values
    
        result.problemValues = numericConverterService().call(
            problemSet.loc[:, config.PROBLEM_SET_INPUT_COLUMN].values,
            result.max_length)
        result.problemOids = problemSet.loc[:, config.PROBLEM_SET_ID_COLUMN].values
        return result
    
    def _calculateMaximumStringLength(self, trainSet, problemSet):
        max_length = max([len(s) for s in trainSet.loc[:, config.TRAINING_SET_INPUT_COLUMN]])
        max_length = max([max_length]+[len(s) for s in problemSet.loc[:, config.PROBLEM_SET_INPUT_COLUMN]])
        return max_length