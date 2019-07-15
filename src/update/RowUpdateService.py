from springboot.Autowired import Autowired
import re
from springboot.Service import Service

config = Autowired('config')
rowProviderService = Autowired('rowProviderService')
transactionDisplayService = Autowired('transactionDisplayService')
updateService = Autowired('updateService')
choiceAskService = Autowired('choiceAskService')
numericConverterService = Autowired('numericConverterService')

@Service
class RowUpdateService:

    def handleOneRow(self, rowNumber, data, connection, categories):
        oidAsStr = str(data.problemOids[rowNumber])
        answers = self.getResultsForRow(rowNumber, data)
        row = rowProviderService.getRowByOid(connection, oidAsStr)
        transactionDisplayService.displayTransaction(row)
        options = self.prepareProbableAnswers(categories, answers)
        choice = self.getChoiceFromUser(options)
        if choice is not None:
            updateService.updateRow(connection, row, oidAsStr, choice)

    def prepareProbableAnswers(self, categories, answers):
        index = 1
        options = {}
        for c in answers:
            if c[1] in categories and c[0] > config.MIN_PROBABILITY:
                print("\t", index, ":", c[0], c[1], categories[c[1]])
                options[index] = c[1], categories[c[1]]
                index += 1
        return options
    
    def getResultsForRow(self,i, data):
        results = []
        for j in range(data.output_neurons):
            results.append((data.problemValues[i][j], j))        
        results = sorted(results, key=lambda rec:rec[0], reverse=True)
        return results

    def getChoiceFromUser(self,options):
        answer = choiceAskService.askUserForChoice()
        choice = self.computeChoiceFromAnswer(options, answer)
        return choice

    def computeChoiceFromAnswer(self,options, answer):
        asNum = numericConverterService.num(answer)
        if asNum in options:
            choice = options[asNum][1]
        elif re.match("\S+,\S+,\S+", answer):
            choice = answer.split(",")
        else:
            choice = None
        return choice
