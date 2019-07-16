from categorizerai.springboot.Autowired import Autowired
from categorizerai.springboot.Service import Service

config = Autowired('config')
@Service
class OptionDisplayService(object):

    def displayOption(self, choiceNumber, probability, categoriesForAnswer):
        print(config.OPTION_DISPLAY_FORMAT.format(choiceNumber, probability, categoriesForAnswer))
