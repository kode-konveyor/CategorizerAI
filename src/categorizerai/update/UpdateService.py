from winterboot.Autowired import Autowired
from winterboot.Service import Service
from categorizerai.ai.AIData import AIData

connectionService = Autowired('ConnectionService')
categoryService = Autowired('CategoryService')
rowUpdateService = Autowired('RowUpdateService')



@Service
class UpdateService:

    def call(self, data: AIData) -> None:
        connection = connectionService.call()
        categories = categoryService.call(connection)
    
        for rowNumber in range(len(data.problemResults)):
            rowUpdateService.call(rowNumber, data, connection, categories)
        connection.close()
