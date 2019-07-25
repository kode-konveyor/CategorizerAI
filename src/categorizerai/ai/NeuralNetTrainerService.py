from winterboot.Autowired import Autowired
from winterboot.Service import Service
import keras
from categorizerai.types.NdArray import NdArray


config = Autowired('Config')()

@Service
class NeuralNetTrainerService:

    def call(self, trainValues: NdArray[float], trainResults: NdArray[int], model: keras.Model) -> float:
        model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        hist = model.fit(trainValues, trainResults, batch_size=config.BATCH_SIZE, epochs=config.EPOCHS, verbose=2)
        accuracy = hist.history.get('acc')[-1]
        return accuracy
