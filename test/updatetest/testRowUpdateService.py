import unittest
from springboot.Autowired import Autowired
from unittest.mock import MagicMock
from springboot.MockedService import MockedService

rowUpdateService = Autowired("rowUpdateService")

class Test(unittest.TestCase):

    def TestName(self):
        data = MagicMock()
        connection = MagicMock()
        categories = MagicMock()
        with MockedService('rowProviderService') as rowProviderService,\
            MockedService('transactionDisplayService') as transactionDisplayService,\
            MockedService('updateDBService') as updateDBService,\
            MockedService('choiceAskService') as choiceAskService,\
            MockedService('numericConverterService') as numericConverterService:
            rowUpdateService.handleOneRow(1,data, connection, categories)

if __name__ == "__main__":
    unittest.main()