import types
from springboot.Service import Service
from springboot.Autowired import Autowired

config = Autowired('config')
numericConverterService = Autowired('numericConverterService')

@Service
class PrepareDataService:

    def prepareData(self, trainSet, problemSet):
        result = types.SimpleNamespace()
        max_length = self.calculateMaximumStringLength(trainSet, problemSet)
        result.numberOfOutputNeurons = max(trainSet.loc[:, config.TRAINING_SET_OUTPUT_COLUMN])+1
    
        result.trainValues = numericConverterService.createNumericArrayFromTextArray(trainSet.loc[:, config.PROBLEM_SET_INPUT_COLUMN].values, max_length)
        result.trainResults = trainSet.loc[:, config.TRAINING_SET_OUTPUT_COLUMN].values
    
        result.problemValues = numericConverterService.createNumericArrayFromTextArray(problemSet.loc[:, config.PROBLEM_SET_INPUT_COLUMN].values, max_length)
        result.problemOids = problemSet.loc[:, config.PROBLEM_SET_ID_COLUMN].values
        return result
    
    def calculateMaximumStringLength(self, trainSet, problemSet):
        max_length = max([len(s) for s in trainSet.loc[:, config.TRAINING_SET_INPUT_COLUMN]])
        max_length = max([max_length]+[len(s) for s in problemSet.loc[:, config.PROBLEM_SET_INPUT_COLUMN]])
        return max_length