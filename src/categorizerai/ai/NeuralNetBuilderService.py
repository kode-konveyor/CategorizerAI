import keras
import tensorflow
from winterboot.Autowired import Autowired
from winterboot.Service import Service

config = Autowired('config')

@Service
class NeuralNetBuilderService:
    def buildNeuralNet(self, max_length, output_neurons):
        model = keras.Sequential([
                    keras.layers.Dense(config.FIRST_LAYER_NEURONS, activation=tensorflow.nn.relu, input_shape=(max_length, )), 
                    keras.layers.Dense(config.SECOND_LAYER_NEURONS, activation=tensorflow.nn.relu), 
                    keras.layers.Dense(output_neurons, activation=tensorflow.nn.softmax)
                ])
        return model