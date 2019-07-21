from winterboot.Stubs import Stubs
from winterboot.TestDataForStub import TestDataForStub

@Stubs
class PrepareDataStubs:
    def behaviour(self, service):
        with\
                TestDataForStub('updateTestData', self):
            service.prepareData.return_value = self.updateTestData.data