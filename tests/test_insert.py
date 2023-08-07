def test_insert_on_row(db):
    assert 1 == db.insert(
        table='users',
        values={'email': 'user1@email.com', 'name': 'user1'})


def test_insert_multiple_lines(db):
    assert 2 == db.insert(
        table='users',
        values=[
            {'email': 'user2@email.com', 'name': 'user2'},
            {'email': 'user3@email.com', 'name': 'user3'}
        ])

