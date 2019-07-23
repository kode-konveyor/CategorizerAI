from winterboot.Service import Service

@Service
class TransactionDisplayService:

    def call(self,row):
        print(row)
