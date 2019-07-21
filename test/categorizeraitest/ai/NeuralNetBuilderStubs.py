from winterboot.TestDataForStub import TestDataForStub
from winterboot.Stubs import Stubs

@Stubs
class NeuralNetBuilderStubs:
    def behaviour(self, service):
        with\
                TestDataForStub('aiTestData') as aiTestData:
            service.buildNeuralNet.return_value = aiTestData.model
