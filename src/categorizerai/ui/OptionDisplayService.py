from winterboot.Autowired import Autowired
from winterboot.Service import Service

config = Autowired('Config')()
@Service
class OptionDisplayService(object):

    def call(self, choiceNumber, probability, categoriesForAnswer):
        print(config.OPTION_DISPLAY_FORMAT.format(choiceNumber, probability, categoriesForAnswer))

