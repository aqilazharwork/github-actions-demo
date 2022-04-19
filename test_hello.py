from hello import add


def test_add():
    assert 2 == add(1, 1)

def kill_add():
    assert 6666 == add(1, 1)