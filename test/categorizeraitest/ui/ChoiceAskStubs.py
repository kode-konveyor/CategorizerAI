from winterboot.Autowired import Autowired
from winterboot.Stubs import Stubs

@Stubs
class ChoiceAskStubs(object):
    def behaviour(self, service):
        pass

    def answerIs(self,choice):
        with Autowired('ChoiceAskService', self):
            self.ChoiceAskService.call.return_value = choice
