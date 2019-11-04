from winterboot.DTO import DTO

@DTO
class AIData(object):
    max_length:int = None
    numberOfOutputNeurons:int = None
    trainValues = None
    trainResults = None
    problemValues = None
    problemOids = None
