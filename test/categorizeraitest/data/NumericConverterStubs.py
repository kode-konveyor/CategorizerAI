from winterboot.Stubs import Stubs
from winterboot.TestDataForStub import TestDataForStub

@Stubs
class NumericConverterStubs:
    def behaviour(self, service):
        with\
                TestDataForStub('UpdateTestData', self):
            service.call.side_effect = ["firstValue", "secondValue"]