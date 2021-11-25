import pytest

def setup():
    global num_a
    if num_a == 0:
        num_a = 2

def es_par(num_a, num_b):
    if num_a%2 == 0 and num_b%2 == 0:
        return True
    else:
        return False

@pytest.mark.smoke
def test_es_par():
    num_a = 2
    num_b = 4
    result = es_par(num_a, num_b)
    assert result , 'Los numerso no son pares'

def test_no_par():
    num_a = 2
    num_b = 4
    result = es_par(num_a, num_b)
    assert result , 'Los numerso son pares'

def teardown():
    global num_a
    if num_a != 0:
        num_a = 0
    