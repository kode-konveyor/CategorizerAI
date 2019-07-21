from winterboot.TestDataForStub import TestDataForStub
from winterboot.Stubs import Stubs

@Stubs
class NeuralNetTrainerStubs:
    def behaviour(self, service):
        with\
                TestDataForStub('aiTestData') as aiTestData:
            service.trainNeuralNet.return_value = aiTestData.ACCURACY
