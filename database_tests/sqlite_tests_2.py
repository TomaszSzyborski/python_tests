import logging
import sqlite3

import time
from collections import namedtuple

import pytest
import pandas as pd


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


@pytest.fixture
def db_CRUD():
    conn = sqlite3.connect("sqlite_from_python.db")
    cursor = conn.cursor()

    def insert_row(data, table_name):
        strigified_data = ",".join([f"{d}" if str(d).isnumeric() else f"'{d}'" for d in data])
        cursor.execute(f"INSERT INTO {table_name} VALUES ({strigified_data})")
        conn.commit()

    def select(data, table_name, where=None, order_by=None):
        conditions = ""
        if where:
            conditions += f"WHERE {where} "
        if order_by:
            conditions += f"ORDER BY{order_by}"
        conditions += ";"

        return cursor.execute(f"SELECT {data} "
                              f"FROM {table_name} "
                              f"{conditions}").fetchall()

    def update(data: dict, table_name, where=None):
        conditions = ""
        if where:
            conditions += f"where {where} "
        conditions += ";"

        stringified_data = "".join([f"{key} = {value}" for key, value in data.items()])

        cursor.execute(f"update {table_name} "
                       f"set {stringified_data}"
                       f"{conditions}")
        conn.commit()

    def delete(q):
        conn.cursor().execute(f"delete {q}")
        conn.commit()

    DB_CRUD = namedtuple("db_CRUD", ["insert_row", "select", "update", "delete"])
    db_crud = DB_CRUD(insert_row, select, update, delete)
    yield db_crud
    conn.close()


# actual tests

def test_select_all_count_rows(db_CRUD, timing):
    dane = pd.DataFrame(db_CRUD.select("*" , "stocks"))
    # db_CRUD.update
    print(dane)
    assert 1 == 1
    logging.info(dane)
