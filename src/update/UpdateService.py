from springboot.Autowired import Autowired
from springboot.Service import Service

connectionFactory = Autowired('connectionFactory')
categoryService = Autowired('categoryService')
rowUpdateService = Autowired('rowUpdateService')

@Service
class UpdateService:

    def handleUpdates(self, data):
        connection = connectionFactory.obtainConnection()
        categories = categoryService.fetchCategories(connection)
    
        for rowNumber in range(len(data.problemResults)):
            rowUpdateService.handleOneRow(rowNumber, data, connection, categories)
        connection.close()
