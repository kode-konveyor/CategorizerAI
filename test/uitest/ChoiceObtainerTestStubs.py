from categorizerai.winterboot.Autowired import Autowired

def choiceObtainerStubs(choice):
    choiceAskService = Autowired('choiceAskService')
    choiceAskService.askUserForChoice.return_value = choice
