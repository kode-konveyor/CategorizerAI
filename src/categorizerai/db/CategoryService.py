from winterboot.Autowired import Autowired
from winterboot.Service import Service

config = Autowired('Config')()

@Service
class CategoryService:

    def call(self, connection):
        cursor = connection.cursor()
        cursor.execute(config.SQL_TO_OBTAIN_CATEGORIES)
        records = cursor.fetchall()
        categories = {}
        for record in records:
            categories[record[config.ID_COLUMN_POSITION_IN_CATEGORIES_TABLE]] = record
        
        cursor.close()
        return categories
