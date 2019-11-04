import unittest
from winterboot.MockedService import MockedService
import TestHelper
from winterboot.Autowired import Autowired

categorizerService = Autowired("CategorizerService")

class testCategorizerService(unittest.TestCase):

    def setUp(self):
        with \
                Autowired('DataTestData', self),\
                Autowired('AiTestData', self),\
                Autowired('UpdateTestData', self),\
                MockedService('PrepareDataService', self),\
                MockedService('NeuralNetBuilderService', self),\
                MockedService('NeuralNetTrainerService', self),\
                MockedService('AccuracyCheckService', self),\
                MockedService('UpdateService', self):
            categorizerService.call()

    def test_it_prepares_data_with_the_loaded_train_set(self):
        TestHelper.assertCallParameter(
            self.DataTestData.TRAIN_SET,
            self.PrepareDataService.call,
            0,
            prepareForCheck=lambda x: x.to_dict())

    def test_it_prepares_data_with_the_loaded_problem_set(self):
        TestHelper.assertCallParameter(
            self.DataTestData.PROBLEM_SET,
            self.PrepareDataService.call, 1,
            prepareForCheck=lambda x: x.to_dict())

    def test_builds_a_neural_net_using_the_computed_max_length(self):
        TestHelper.assertCallParameter(
            self.UpdateTestData.data.max_length,
            self.NeuralNetBuilderService.call, 0)

    def test_builds_a_neural_net_using_the_computed_number_of_output_neurons(self):
        TestHelper.assertCallParameter(
            self.UpdateTestData.data.numberOfOutputNeurons,
            self.NeuralNetBuilderService.call, 1)

    def test_trains_the_built_model(self):
        TestHelper.assertCallParameter(self.AiTestData.model,
                    self.NeuralNetTrainerService.call, 2)

    def test_trains_the_built_model_using_training_values(self):
        TestHelper.assertCallParameter(self.UpdateTestData.data.trainValues,
                    self.NeuralNetTrainerService.call, 0)

    def test_trains_the_built_model_using_training_results(self):
        TestHelper.assertCallParameter(self.UpdateTestData.data.trainResults,
                    self.NeuralNetTrainerService.call, 1)
    
    def test_uses_the_trained_neural_net_to_get_the_predictions_from_problemValues(self):
        TestHelper.assertCallParameter(self.UpdateTestData.data.problemValues,
                    self.AiTestData.model.predict, 0)

    def test_checks_the_accuracy_of_the_built_modell(self):
        TestHelper.assertCallParameter(self.AiTestData.ACCURACY, self.AccuracyCheckService.call, 0)

    def test_updates_categories_based_on_predictions(self):
        TestHelper.assertCallParameter(self.UpdateTestData.data,
                    self.UpdateService.call, 0)
    

if __name__ == "__main__":
    unittest.main()
