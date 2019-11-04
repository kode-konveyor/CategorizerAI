#coding=utf-8
import unittest
from winterboot.Autowired import Autowired
import keras
import tensorflow
import TestHelper
from winterboot.MockedService import MockedService

neuralNetBuilderService = Autowired('NeuralNetBuilderService')
config = Autowired('Config')()

class testNeuralNetBuilderService(unittest.TestCase):

    def setUp(self):
        with\
                Autowired('DataTestData', self),\
                MockedService('keras.Sequential') as self.model:
            self.result = neuralNetBuilderService().call(self.DataTestData.MAX_LENGTH, self.DataTestData.OUTPUT_NEURONS )
        self.firstCallList = TestHelper.callArgument(self.model, 0)

    def test_it_builds_a_Sequential_model(self):
        self.model.assert_called_once()
    def test_first_layer_is_Dense(self):
        self.assertEqual(keras.layers.Dense, type(self.firstCallList[0]))
    def test_first_layer_have_FIRST_LAYER_NEURONS_number_of_neurons(self):
        self.assertEqual(config.FIRST_LAYER_NEURONS, self.firstCallList[0].units)
    def test_first_layer_have_relu_activation(self):
        self.assertEqual(tensorflow.nn.relu, self.firstCallList[0].activation)
    def test_second_layer_is_Dense(self):
        self.assertEqual(keras.layers.Dense, type(self.firstCallList[1]))
    def test_second_layer_have_SECOND_LAYER_NEURONS_number_of_neurons(self):
        self.assertEqual(config.SECOND_LAYER_NEURONS, self.firstCallList[1].units)
    def test_second_layer_have_relu_activation(self):
        self.assertEqual(tensorflow.nn.relu, self.firstCallList[1].activation)
    def test_third_layer_is_Dense(self):
        self.assertEqual(keras.layers.Dense, type(self.firstCallList[2]))
    def test_third_layer_have_output_neurons_number_of_neurons(self):
        self.assertEqual(self.DataTestData.OUTPUT_NEURONS, self.firstCallList[2].units)
    def test_third_layer_have_softmax_activation(self):
        self.assertEqual(tensorflow.nn.softmax, self.firstCallList[2].activation)
