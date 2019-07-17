import unittest
from winterboot.Autowired import Autowired
from winterboot.MockedService import MockedService
import TestHelper
from categorizeraitest.data.DataTestData import DataTestData


categorizerService = Autowired("categorizerService")
class Test(unittest.TestCase):

    def setUp(self):
        with \
                MockedService('prepareDataService') as prepareDataService,\
                MockedService('neuralNetBuilderService') as neuralNetBuilderService,\
                MockedService('neuralNetTrainerService') as neuralNetTrainerService,\
                MockedService('accuracyCheckService') as accuracyCheckService,\
                MockedService('updateDBService') as updateDBService:
            self.prepareDataService = prepareDataService
            categorizerService.categorize()

    def test_categorize_prepares_data_with_the_loaded_train_set(self):
        TestHelper.assertCallParameter(DataTestData.TRAIN_SET, self.prepareDataService.prepareData, 0, prepareForCheck=lambda x: x.to_dict())

    def test_categorize_prepares_data_with_the_loaded_problem_set(self):
        TestHelper.assertCallParameter(DataTestData.PROBLEM_SET, self.prepareDataService.prepareData, 1, prepareForCheck=lambda x: x.to_dict())

if __name__ == "__main__":
    unittest.main()
print("testCategorizerService end")
