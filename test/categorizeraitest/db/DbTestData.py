# coding=utf-8
from unittest.mock import MagicMock
from winterboot.Service import Service

@Service
class DbTestData: 
    def __init__(self):
        self.oidAsString = "1115"
        self.connectKwArgs = {
            'database': 'transactions',
            'user': 'username',
            'password': 's3cr3t',
            'host': 'example.com',
            'port': 5432
            }
        self.all_rows = [
            (1112, "abc", 11.12, "a", "b" ),
            (1113, "cő", -11.13, "d", "e" ),
            (1114, "efgh", -11.14, "d", "e" ),
            (1118, "baz", -11.18, "e", "f" ),
            (1115, "boo", 11.15, None , None ),
            (1116, "fefefe", -11.16, None, None )
            ]
        self.trainRows = self.all_rows[:4]
        self.trainComments = map(lambda x: x[1], self.trainRows)
        self.problemRows = self.all_rows[4:]
        self.problemOids = map(lambda x: x[0], self.problemRows)
        self.problemComments = map(lambda x: x[1], self.problemRows)
        self.fetched_row = self.all_rows[3]
        self.choice = ("foo", "bar", "baz")
        self.formattedUpdateQuery = "update transactions set category1='bar', category2='baz' where oid=1115"
        self.connection = None
        self.connector = None
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

