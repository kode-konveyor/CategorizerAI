#coding=utf-8
import unittest
from springboot.Autowired import Autowired
from datatest import DataTestHelper
import keras
import tensorflow

neuralNetBuilderService = Autowired('neuralNetBuilderService')
config = Autowired('config')

class Test(unittest.TestCase):

    def setUp(self):
        with unittest.mock.patch('keras.Sequential') as self.model:
            self.result = neuralNetBuilderService.buildNeuralNet(DataTestHelper.MAX_LENGTH, DataTestHelper.OUTPUT_NEURONS )
        self.firstCallList = self.model.call_args_list[0][0][0]

    def test_buildNeuralNet_builds_a_Sequential_model(self):
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
        self.assertEqual(DataTestHelper.OUTPUT_NEURONS, self.firstCallList[2].units)
    def test_third_layer_have_softmax_activation(self):
        self.assertEqual(tensorflow.nn.softmax, self.firstCallList[2].activation)
