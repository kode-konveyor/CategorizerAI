import keras
import tensorflow
from winterboot.Autowired import Autowired
from winterboot.Service import Service

config = Autowired('Config')()

@Service
class NeuralNetBuilderService:
    def call(self, max_length: int, numberOfOutputNeurons: int ) -> keras.Model:
        model = keras.Sequential([
                    keras.layers.Dense(config.FIRST_LAYER_NEURONS, activation=tensorflow.nn.relu, input_shape=(max_length, )), 
                    keras.layers.Dense(config.SECOND_LAYER_NEURONS, activation=tensorflow.nn.relu), 
                    keras.layers.Dense(numberOfOutputNeurons, activation=tensorflow.nn.softmax)
                ])
        return model