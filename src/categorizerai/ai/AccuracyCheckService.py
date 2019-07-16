
import sys
from categorizerai.winterboot.Autowired import Autowired
from categorizerai.winterboot.Service import Service

config = Autowired('config')
displayAccuracyService = Autowired('displayAccuracyService')
accuracyErrorDisplayService = Autowired('accuracyErrorDisplayService')

@Service
class AccuracyCheckService:
    
    def checkAccuracy(self, accuracy):

        displayAccuracyService.displayAccuracy(accuracy)
        if accuracy < config.MIN_ACCURACY:
            accuracyErrorDisplayService.displayAccurracyError()
            sys.exit(-1)

