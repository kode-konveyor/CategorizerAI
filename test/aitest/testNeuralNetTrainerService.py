#coding=utf-8
import unittest
from springboot.Autowired import Autowired
from aitest import AiTestHelper
from unittest.mock import MagicMock

neuralNetTrainerService = Autowired('neuralNetTrainerService')
config = Autowired('config')

class Test(unittest.TestCase):

    def setUp(self):
        self.model = MagicMock()
        history = MagicMock()
        self.model.fit.return_value = history
        history.history.get.return_value = [AiTestHelper.ACCURACY]
        self.result = neuralNetTrainerService.trainNeuralNet(
            AiTestHelper.TRAIN_VALUES,
            AiTestHelper.TRAIN_RESULTS,
            self.model)
        self.compileCallKwargs = self.model.compile.call_args_list[0][1]
        self.fitCallArgs = self.model.fit.call_args_list[0][0]
        self.fitCallKwargs = self.model.fit.call_args_list[0][1]

    def test_trainNeuralNet_compiles_the_model(self):
        self.model.compile.assert_called_once()

    def test_trainNeuralNet_returns_model_accuracy(self):
        self.assertEquals(AiTestHelper.ACCURACY, self.result)

    def test_loss_funtions_is_sparse_categorical_crossentropy(self):
        self.assertEquals("sparse_categorical_crossentropy", self.compileCallKwargs['loss'])

    def test_optimizer_is_adam(self):
        self.assertEquals("adam", self.compileCallKwargs['optimizer'])

    def test_metric_is_accuracy(self):
        self.assertEquals(["accuracy"], self.compileCallKwargs['metrics'])

    def test_trainNeuralNet_fits_the_model(self):
        self.model.fit.assert_called_once()

    def test_fit_uses_train_values(self):
        self.assertEquals(AiTestHelper.TRAIN_VALUES, self.fitCallArgs[0])

    def test_fit_uses_train_results(self):
        self.assertEquals(AiTestHelper.TRAIN_RESULTS, self.fitCallArgs[1])

    def test_batch_size_is_BATCH_SIZE(self):
        self.assertEquals(config.BATCH_SIZE, self.fitCallKwargs['batch_size'])

    def test_number_of_epochs_is_EPOCHS(self):
        self.assertEquals(config.EPOCHS, self.fitCallKwargs['epochs'])

