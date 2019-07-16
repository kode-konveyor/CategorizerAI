from categorizerai.springboot.Autowired import Autowired

def choiceObtainerStubs(choice):
    choiceAskService = Autowired('choiceAskService')
    choiceAskService.askUserForChoice.return_value = choice
