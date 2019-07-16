from unittest.mock import MagicMock
from categorizerai.springboot import SpringBoot

class MockedService(object):
    def __init__(self, serviceName):
        self.serviceName = serviceName
        self.mock = MagicMock()
        self.orig = SpringBoot.providers[serviceName][0]
        SpringBoot.providers[serviceName][0]=self.mock
        SpringBoot.wireOneService(serviceName)

    def __enter__(self):
        return self.mock

    def __exit__(self, exceptionType, value, traceback):
        SpringBoot.providers[self.serviceName][0] = self.orig
        SpringBoot.wireOneService(self.serviceName)
        if exceptionType is not None:
            raise value

