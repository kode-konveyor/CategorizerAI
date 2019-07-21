import unittest
from winterboot.MockedService import MockedService
import TestHelper
from winterboot.Autowired import Autowired

categorizerService = Autowired("categorizerService")

class Test(unittest.TestCase):

    def setUp(self):
        with \
                Autowired('dataTestData', self),\
                Autowired('aiTestData', self),\
                Autowired('updateTestData', self),\
                MockedService('prepareDataService', self),\
                MockedService('neuralNetBuilderService', self),\
                MockedService('neuralNetTrainerService', self),\
                MockedService('accuracyCheckService', self),\
                MockedService('updateService', self):
            categorizerService().categorize()

    def test_categorize_prepares_data_with_the_loaded_train_set(self):
        TestHelper.assertCallParameter(
            self.dataTestData.TRAIN_SET,
            self.prepareDataService.prepareData,
            0,
            prepareForCheck=lambda x: x.to_dict())

    def test_categorize_prepares_data_with_the_loaded_problem_set(self):
        TestHelper.assertCallParameter(
            self.dataTestData.PROBLEM_SET,
            self.prepareDataService.prepareData, 1,
            prepareForCheck=lambda x: x.to_dict())

    def test_builds_a_neural_net_using_the_computed_max_length(self):
        TestHelper.assertCallParameter(
            self.updateTestData.data.max_length,
            self.neuralNetBuilderService.buildNeuralNet, 0)

    def test_builds_a_neural_net_using_the_computed_number_of_output_neurons(self):
        TestHelper.assertCallParameter(
            self.updateTestData.data.numberOfOutputNeurons,
            self.neuralNetBuilderService.buildNeuralNet, 1)

    def test_trains_the_built_model(self):
        TestHelper.assertCallParameter(self.aiTestData.model,
                    self.neuralNetTrainerService.trainNeuralNet, 2)

    def test_trains_the_built_model_using_training_values(self):
        TestHelper.assertCallParameter(self.updateTestData.data.trainValues,
                    self.neuralNetTrainerService.trainNeuralNet, 0)

    def test_trains_the_built_model_using_training_results(self):
        TestHelper.assertCallParameter(self.updateTestData.data.trainResults,
                    self.neuralNetTrainerService.trainNeuralNet, 1)
    
    def test_uses_the_trained_neural_net_to_get_the_predictions_from_problemValues(self):
        TestHelper.assertCallParameter(self.updateTestData.data.problemValues,
                    self.aiTestData.model.predict, 0)

    def test_checks_the_accuracy_of_the_built_modell(self):
        TestHelper.assertCallParameter(self.aiTestData.ACCURACY, self.accuracyCheckService.checkAccuracy, 0)

    def test_updates_categories_based_on_predictions(self):
        TestHelper.assertCallParameter(self.updateTestData.data,
                    self.updateService.handleUpdates, 0)
    

if __name__ == "__main__":
    unittest.main()
