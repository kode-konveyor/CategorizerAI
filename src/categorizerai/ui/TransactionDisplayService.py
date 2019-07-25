from winterboot.Service import Service
from typing import Tuple

@Service
class TransactionDisplayService:

    def call(self,row: Tuple) -> None:
        print(row)
