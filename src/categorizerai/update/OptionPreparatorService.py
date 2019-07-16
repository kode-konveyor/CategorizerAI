from categorizerai.winterboot.Autowired import Autowired
from categorizerai.winterboot.Service import Service

config = Autowired('config')
optionDisplayService = Autowired('optionDisplayService')
@Service
class OptionPreparatorService:

    def prepareOptionsToOffer(self, rowNumber, data, categories):
        answers = self.getAnswersForRow(rowNumber, data)
        options = self.prepareProbableAnswers(categories, answers)
        return options
    
    def getAnswersForRow(self,rowNumber, data):
        results = []
        row = data.problemValues[rowNumber]
        for j in range(data.output_neurons):
            results.append((row[j], j))
        results = sorted(results, key=lambda rec:rec[0], reverse=True)
        return results

    def prepareProbableAnswers(self, categories, answers):
        choiceNumber = 1
        options = {}
        for answer in answers:
            probability = answer[0]
            categoryId = answer[1]
            if categoryId in categories and probability > config.MIN_PROBABILITY:
                categoriesForAnswer = categories[categoryId]
                optionDisplayService.displayOption(choiceNumber, probability, categoriesForAnswer)
                options[choiceNumber] = probability, categoriesForAnswer
                choiceNumber += 1
        return options

