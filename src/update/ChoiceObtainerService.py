from springboot.Autowired import Autowired
import re
from springboot.Service import Service

choiceAskService = Autowired('choiceAskService')
numericConverterService = Autowired('numericConverterService')

@Service
class ChoiceObtainerService:

    def obtainChoice(self,options):
        answer = choiceAskService.askUserForChoice()
        choice = self.computeChoiceFromAnswer(options, answer)
        return choice

    def computeChoiceFromAnswer(self,options, answer):
        asNum = numericConverterService.num(answer)
        if asNum in options:
            choice = options[asNum][1]
        elif re.match("\S+,\S+,\S+", answer):
            choice = answer.split(",")
        else:
            choice = None
        return choice
