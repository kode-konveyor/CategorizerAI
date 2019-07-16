import unittest
from winterboot.Autowired import Autowired
from winterboot.MockedService import MockedService

categorizerService = Autowired("categorizerService")
class Test(unittest.TestCase):

    def testName(self):
        with \
                MockedService('prepareDataService') as prepareDataService,\
                MockedService('neuralNetBuilderService') as neuralNetBuilderService,\
                MockedService('neuralNetTrainerService') as neuralNetTrainerService,\
                MockedService('accuracyCheckService') as accuracyCheckService,\
                MockedService('updateDBService') as updateDBService:
            categorizerService.categorize()

if __name__ == "__main__":
    unittest.main()