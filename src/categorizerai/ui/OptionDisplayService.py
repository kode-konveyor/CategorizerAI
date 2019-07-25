from winterboot.Autowired import Autowired
from winterboot.Service import Service
from typing import List

config = Autowired('Config')()
@Service
class OptionDisplayService(object):

    def call(self, choiceNumber: int, probability: float, categoriesForAnswer: List[str]) -> None:
        print(config.OPTION_DISPLAY_FORMAT.format(choiceNumber, probability, categoriesForAnswer))

