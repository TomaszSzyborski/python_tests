import logging
import sqlite3
# import os
# from sqlite3 import Error
import time
from pprint import pprint
import pytest
import pandas as pd


# from faker import Faker
# from random import choice

@pytest.fixture
def timing(request):
    logging.basicConfig(level=logging.INFO)
    request.started_at = time.time()

    # request.time_to_execute = None

    def log_time():
        time_to_execute = time.time() - request.started_at
        logging.info(f"{request.node.name} took "
                     f"{time_to_execute:.3f} s to execute.")

    request.addfinalizer(log_time)


# def create_db():
#     db_file = "sqlite_from_python.db"
#     if not os.path.isfile(db_file):
#         try:
#             conn = sqlite3.connect(db_file)
#             print(sqlite3.version)
#         except Error as e:
#             print(e)
#         finally:
#             conn.close()
#     else:
#         print("DB already exists")
#
#
# def create_table(conn, cursor, table_name, table_headers):
#     """
#     :param cursor: connection cursor
#     :param table_name: name of table to create in database
#     :param table_headers: headers names as list
#     :return:
#     """
#     strigified_data = ",".join(table_headers)
#     cursor.execute(f"CREATE TABLE {table_name} ({strigified_data})")
#     conn.commit()
#
#
# def insert_row(conn, cursor, table_name, data):
#     strigified_data = ",".join([f"{d}" if str(d).isnumeric() else f"'{d}'" for d in data])
#     cursor.execute(f"INSERT INTO {table_name} VALUES ({strigified_data})")
#     conn.commit()

@pytest.fixture
def query():
    conn = sqlite3.connect("sqlite_from_python.db")
    yield lambda q: conn.cursor().execute(q).fetchall()
    conn.close()


def test_select_all_count_rows(query, timing):
    dane = pd.DataFrame(query("Select * from stocks"))
    print(dane)
    assert 1 == 1
    logging.info(dane)
