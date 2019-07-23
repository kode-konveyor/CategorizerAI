from winterboot.Stubs import Stubs
from winterboot.TestDataForStub import TestDataForStub

@Stubs
class RowProviderStubs:
    def behaviour(self, service):
        with\
                TestDataForStub('DbTestData', self):
            service.call.return_value = self.DbTestData.fetched_row