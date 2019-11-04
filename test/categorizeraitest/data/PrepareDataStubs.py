from winterboot.Stubs import Stubs
from winterboot.TestDataForStub import TestDataForStub

@Stubs
class PrepareDataStubs:
    def behaviour(self, service):
        with\
                TestDataForStub('UpdateTestData', self):
            service.call.return_value = self.UpdateTestData.data