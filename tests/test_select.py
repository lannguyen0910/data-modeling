import pytest


@pytest.mark.parametrize("table_name", ["artists", "songplays", "songs", "time", "users"])
def test_select_query(mysql_connection, table_name):
    cursor = mysql_connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
    result = cursor.fetchall()
    assert len(result) > 0
    cursor.close()
