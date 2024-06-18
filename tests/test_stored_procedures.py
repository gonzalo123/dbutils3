from dbutils.dbutils import Db


def test_call_stored_procedure_fetch_one(cursor):
    db = Db(cursor=cursor)
    assert 'Hello Gonzalo' == db.sp_fetch_one(
        function='hello',
        params={'name': 'Gonzalo'})


def test_call_stored_procedure_fetch_all(cursor):
    db = Db(cursor=cursor)
    assert 'Hello Gonzalo' == db.sp_fetch_all(
        function='hello',
        params={'name': 'Gonzalo'})[0]['hello']


def test_call_stored_procedure_fetch_all_with_out(cursor):
    db = Db(cursor=cursor)
    response = db.sp_fetch_all(
        function='hello2',
        params={'name': 'Gonzalo'},
        out=True
    )
    assert 'Hello Gonzalo' == response[0]['name2']
