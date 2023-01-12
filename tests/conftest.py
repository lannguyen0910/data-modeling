import mysql.connector
import pytest

from configs import HOST, USER, PASSWD, DATABASE, AUTH_PLUGIN


@pytest.fixture
def mysql_connection():
    print(f'User: {USER} | Host: {HOST}')
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWD,
        database=DATABASE,
        auth_plugin=AUTH_PLUGIN
    )

    yield connection
    connection.close()
