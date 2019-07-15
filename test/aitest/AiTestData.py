from unittest.mock import MagicMock

class AITestData:
    ACCURACY = 0.78
    LOW_ACCURACY = 0.55
    TRAIN_VALUES = "train_values"
    TRAIN_RESULTS = "train_results"
    model = None

    def __init__(self):
        model = MagicMock()
        history = MagicMock()
        model.fit.return_value = history
        history.history.get.return_value = [self.ACCURACY]
        self.model = model

