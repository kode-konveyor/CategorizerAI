# coding=utf-8
from unittest.mock import MagicMock

class DbTestData:
    
    oidAsString = "1115"
    connectKwArgs = {
        'database': 'transactions',
        'user': 'username',
        'password': 's3cr3t',
        'host': 'example.com',
        'port': 5432
        }
    all_rows = [
        (1112, "abc", 11.12, "a", "b" ),
        (1113, "cő", -11.13, "d", "e" ),
        (1114, "efgh", -11.14, "d", "e" ),
        (1118, "baz", -11.18, "e", "f" ),
        (1115, "boo", 11.15, None , None ),
        (1116, "fefefe", -11.16, None, None )
        ]
    trainRows = all_rows[:4]
    trainComments = map(lambda x: x[1], trainRows)
    problemRows = all_rows[4:]
    problemOids = map(lambda x: x[0], problemRows)
    problemComments = map(lambda x: x[1], problemRows)
    fetched_row = all_rows[3]
    choice = ("foo", "bar", "baz")
    formattedUpdateQuery = "update transactions set category1='bar', category2='baz' where oid=1115"
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

