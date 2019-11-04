from winterboot.Autowired import Autowired
from winterboot.Service import Service
from categorizerai.ai.AIData import AIData
import psycopg2

rowProviderService = Autowired('RowProviderService')
transactionDisplayService = Autowired('TransactionDisplayService')
updateDBService = Autowired('UpdateDBService')
optionPreparatorService = Autowired('OptionPreparatorService')
choiceObtainerService = Autowired('ChoiceObtainerService')

@Service
class RowUpdateService:

    def call(self, rowNumber:int, data:AIData, connection:psycopg2.extensions.connection, categories:tuple) -> None:
        oidAsStr = str(data.problemOids[rowNumber])
        row = rowProviderService.call(connection, oidAsStr)
        transactionDisplayService.call(row)
        options = optionPreparatorService.call(rowNumber, data, categories)
        choice = choiceObtainerService.call(options)
        if choice is not None:
            updateDBService.call(connection, oidAsStr, row, choice)
