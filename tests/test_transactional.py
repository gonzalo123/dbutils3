import psycopg
from dbutils import transactional, get_cursor, Db, transactional_cursor
from tests.sql import SQL_COUNT


def test_simple_transaction(conn):
    cursor = get_cursor(conn=conn)
    db2 = Db(cursor=cursor)

    with transactional(conn) as db:
        # assert isinstance(db.get_cursor(), Cursor)
        assert 1 == db.insert(
            table='users',
            values={'email': 'user1@email.com', 'name': 'user1'})

    assert 1 == db2.fetch_one(sql=SQL_COUNT)


def test_transaction_exception_rollback(conn):
    cursor = get_cursor(conn=conn)
    db2 = Db(cursor=cursor)
    assert 0 == db2.fetch_one(sql=SQL_COUNT)

    with transactional(conn) as db:
        # assert isinstance(db.get_cursor(), Cursor)
        assert 1 == db.insert(
            table='users',
            values={'email': 'user1@email.com', 'name': 'user1'})
    assert 1 == db2.fetch_one(sql=SQL_COUNT)

    try:
        with transactional_cursor(conn) as cursor:
            db = Db(cursor)
            db.insert(
                table='users',
                values={'email': 'user1@email.com', 'name': 'user1'})
    except psycopg.Error as e:
        assert isinstance(e, psycopg.errors.UniqueViolation)

    with transactional(conn) as db:
        assert 1 == db.insert(
            table='users',
            values={'email': 'user2@email.com', 'name': 'user2'})
    assert 2 == db2.fetch_one(sql=SQL_COUNT)
