from unittest.mock import MagicMock

class DbTestData:
    
    oidAsString = "10"
    all_rows = [
        ("first row 1", "first row 2", "first row 3", "first row 4", ),
        ("second row 1", "second row 2", "second row 3", "second row 4", ),
        ("third row 1", "third row 2", "third row 3", "third row 4", )
        ]
    fetched_row = all_rows[1]
    choice = ("foo", "bar", "baz")
    formattedUpdateQuery = "update transactions set category1='bar', category2='baz' where oid=10"
    connection = None
    connector = None
    
    def __init__(self):
        self.connection, self.connector = self.databaseConnectorMock()

    def connectionMock(self):
        connection = MagicMock()
        connection.cursor = MagicMock()
        connection.cursor.return_value = connection.cursor
        connection.cursor.fetchone = MagicMock(return_value=self.fetched_row)
        connection.cursor.fetchall = MagicMock(return_value=self.all_rows)
        connection.cursor.close = MagicMock()
        connection.cursor.execute = MagicMock()
        return connection
    
    def databaseConnectorMock(self):
        connection = self.connectionMock()
        connector = MagicMock(return_value=connection)
        return connection, connector

