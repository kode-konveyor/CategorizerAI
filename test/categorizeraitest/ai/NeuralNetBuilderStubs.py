from winterboot.Autowired import Autowired

def behaviour(aiTestData):
        neuralNetBuilderService = Autowired('neuralNetBuilderService')()
        neuralNetBuilderService.buildNeuralNet.return_value = aiTestData.model
