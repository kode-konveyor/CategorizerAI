import re
from winterboot.Autowired import Autowired
from winterboot.Service import Service

config = Autowired('Config')()
choiceAskService = Autowired('ChoiceAskService')

@Service
class ChoiceObtainerService:

    def call(self,options):
        answer = choiceAskService.call()
        choice = self._computeChoiceFromAnswer(options, answer)
        return choice

    def _computeChoiceFromAnswer(self,options, answer):
        asNum = self._num(answer)
        if asNum in options:
            choice = options[asNum][1]
        elif re.match(config.CHOICE_FORMAT_REGEX, answer):
            choice = answer.split(",")
        else:
            choice = None
        return choice

    def _num(self,s):
        try:
            return int(s)
        except ValueError:
            return None

