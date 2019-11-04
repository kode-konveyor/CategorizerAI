from winterboot.TestDataForStub import TestDataForStub
from winterboot.Stubs import Stubs

@Stubs
class NeuralNetBuilderStubs:
    def behaviour(self, service):
        with\
                TestDataForStub('AiTestData') as AiTestData:
            service.call.return_value = AiTestData.model
