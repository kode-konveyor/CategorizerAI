from winterboot.Service import Service

ACCURACY_ERROR_MESSAGE = "Accuracy is too small, exiting. Try again."

@Service
class AccuracyErrorDisplayService:
    
    def call(self):
        return print(ACCURACY_ERROR_MESSAGE)
