
import sys
from winterboot.Autowired import Autowired
from winterboot.Service import Service

config = Autowired('Config')()
displayAccuracyService = Autowired('DisplayAccuracyService')
accuracyErrorDisplayService = Autowired('AccuracyErrorDisplayService')

@Service
class AccuracyCheckService:
    
    def call(self, accuracy: float) -> None:

        displayAccuracyService.call(accuracy)
        if accuracy < config.MIN_ACCURACY:
            accuracyErrorDisplayService.call()
            sys.exit(-1)

