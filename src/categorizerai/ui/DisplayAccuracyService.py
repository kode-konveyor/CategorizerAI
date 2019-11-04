from winterboot.Service import Service

ACCURACY_STRING = "accuracy:{0}"

@Service
class DisplayAccuracyService:
    
    def call(self,accuracy: float):
        return print(ACCURACY_STRING.format(str(accuracy)))

