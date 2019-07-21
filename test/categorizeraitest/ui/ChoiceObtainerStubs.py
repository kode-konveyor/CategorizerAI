from winterboot.Autowired import Autowired

def choiceObtainerStubs(choice):
    with Autowired('choiceAskService') as choiceAskService:
        choiceAskService.askUserForChoice.return_value = choice
