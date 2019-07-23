from winterboot.DTO import DTO

@DTO
class AIData(object):
    max_length = None
    numberOfOutputNeurons = None
    trainValues = None
    trainResults = None
    problemValues = None
    problemOids = None
