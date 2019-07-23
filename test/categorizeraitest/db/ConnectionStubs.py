from winterboot.Stubs import Stubs
from winterboot.TestDataForStub import TestDataForStub

@Stubs
class ConnectionStubs:
    def behaviour(self, service):
        with\
                TestDataForStub('DbTestData', self):
            service.call.return_value = self.DbTestData.connection
