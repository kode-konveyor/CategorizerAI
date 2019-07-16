from categorizerai.springboot.Autowired import Autowired
from categorizerai.springboot.Service import Service

connectionService = Autowired('connectionService')
categoryService = Autowired('categoryService')
rowUpdateService = Autowired('rowUpdateService')

@Service
class UpdateService:

    def handleUpdates(self, data):
        connection = connectionService.obtainConnection()
        categories = categoryService.fetchCategories(connection)
    
        for rowNumber in range(len(data.problemResults)):
            rowUpdateService.handleOneRow(rowNumber, data, connection, categories)
        connection.close()