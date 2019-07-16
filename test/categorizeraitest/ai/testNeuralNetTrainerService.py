#coding=utf-8
import unittest
from winterboot.Autowired import Autowired
from categorizeraitest.ai.AiTestData import AITestData
import TestHelper

neuralNetTrainerService = Autowired('neuralNetTrainerService')
config = Autowired('config')

class Test(unittest.TestCase):

    def setUp(self):
        self.aiTestData = AITestData()
        self.model = self.aiTestData.model

        self.result = neuralNetTrainerService.trainNeuralNet(
            self.aiTestData.TRAIN_VALUES,
            self.aiTestData.TRAIN_RESULTS,
            self.model)
        self.compileCallKwargs = TestHelper.callKwArgument(self.model.compile)
        self.fitCallKwargs = TestHelper.callKwArgument(self.model.fit)

    def test_trainNeuralNet_compiles_the_model(self):
        self.model.compile.assert_called_once()

    def test_trainNeuralNet_returns_model_accuracy(self):
        self.assertEqual(self.aiTestData.ACCURACY, self.result)

    def test_loss_funtions_is_sparse_categorical_crossentropy(self):
        self.assertEqual("sparse_categorical_crossentropy", self.compileCallKwargs['loss'])

    def test_optimizer_is_adam(self):
        self.assertEqual("adam", self.compileCallKwargs['optimizer'])

    def test_metric_is_accuracy(self):
        self.assertEqual(["accuracy"], self.compileCallKwargs['metrics'])

    def test_trainNeuralNet_fits_the_model(self):
        self.model.fit.assert_called_once()

    def test_fit_uses_train_values(self):
        self.assertEqual(self.aiTestData.TRAIN_VALUES, TestHelper.callArgument(self.model.fit,0))

    def test_fit_uses_train_results(self):
        self.assertEqual(self.aiTestData.TRAIN_RESULTS, TestHelper.callArgument(self.model.fit,1))

    def test_batch_size_is_BATCH_SIZE(self):
        self.assertEqual(config.BATCH_SIZE, self.fitCallKwargs['batch_size'])

    def test_number_of_epochs_is_EPOCHS(self):
        self.assertEqual(config.EPOCHS, self.fitCallKwargs['epochs'])
