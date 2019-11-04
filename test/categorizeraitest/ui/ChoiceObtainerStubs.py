from winterboot.Stubs import Stubs

@Stubs
class ChoiceObtainerStubs(object):
    def behaviour(self, service):
        self.service = service

    def answerIs(self,choice):
        self.service.call.return_value = choice
