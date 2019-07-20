from winterboot.Autowired import Autowired

def behaviour(aiTestData):
        neuralNetTrainerService = Autowired('neuralNetTrainerService')()
        neuralNetTrainerService.trainNeuralNet.return_value = aiTestData.ACCURACY
