import unittest
from dbtest import DbTestHelper

def allStubs():
    connection = unittest.mock.MagicMock()
    connection.cursor = unittest.mock.MagicMock()
    connection.cursor.return_value = connection.cursor
    connection.cursor.fetchone = unittest.mock.MagicMock(return_value=DbTestHelper.fetched_row)
    connection.cursor.fetchall = unittest.mock.MagicMock(return_value=DbTestHelper.all_rows)
    connection.cursor.close = unittest.mock.MagicMock()
    connection.cursor.execute = unittest.mock.MagicMock()
    return connection
