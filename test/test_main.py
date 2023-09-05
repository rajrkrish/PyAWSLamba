from mathops.main import addition


def test_addition():
    assert addition(10,5) == 15
    assert addition(11, 5) != 15