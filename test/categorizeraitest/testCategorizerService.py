import unittest
from winterboot.Autowired import Autowired
from winterboot.MockedService import MockedService
import TestHelper
from categorizeraitest.data.DataTestData import DataTestData
from categorizeraitest.update.UpdateTestData import UpdateTestData
from categorizeraitest.ai.AiTestData import AITestData


categorizerService = Autowired("categorizerService")
class Test(unittest.TestCase):

    def setUp(self):
        self.testData = DataTestData()
        self.updateTestData = UpdateTestData()
        self.aiTestData = AITestData()
        with \
                MockedService('prepareDataService') as prepareDataService,\
                MockedService('neuralNetBuilderService') as neuralNetBuilderService,\
                MockedService('neuralNetTrainerService') as neuralNetTrainerService,\
                MockedService('accuracyCheckService') as accuracyCheckService,\
                MockedService('updateService') as updateService:
            self.prepareDataService = prepareDataService
            self.neuralNetBuilderService = neuralNetBuilderService
            self.neuralNetTrainerService = neuralNetTrainerService
            self.accuracyCheckService = accuracyCheckService
            self.updateService = updateService

            self.prepareDataService.prepareData.return_value = self.updateTestData.data
            self.neuralNetBuilderService.buildNeuralNet.return_value = self.aiTestData.model
            self.neuralNetTrainerService.trainNeuralNet.return_value = self.aiTestData.ACCURACY

            categorizerService.categorize()

    def test_categorize_prepares_data_with_the_loaded_train_set(self):
        TestHelper.assertCallParameter(
            self.testData.TRAIN_SET,
            self.prepareDataService.prepareData,
            0,
            prepareForCheck=lambda x: x.to_dict())

    def test_categorize_prepares_data_with_the_loaded_problem_set(self):
        TestHelper.assertCallParameter(
            self.testData.PROBLEM_SET,
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
