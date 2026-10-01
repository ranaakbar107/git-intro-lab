from calculator import add, subtract

def test_add():
    assert add(4, 1) == 5

def test_subtract():
    assert subtract(8, 6) == 2