from unittest.mock import MagicMock
from springboot import SpringBoot
from springboot.Autowired import Autowired
class MockedService(object):
    def __init__(self, serviceName):
        self.mock = MagicMock()
        SpringBoot.providers[serviceName][0]=self.mock
        Autowired.wire()
    def __enter__(self):
        return self.mock
    def __exit__(self, exceptionType, value, traceback):
        if exceptionType is not None:
            raise value
