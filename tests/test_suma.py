
def suma(a, b):
    return a + b

def test_suma_correcta():
    assert suma(2, 3) == 5

def test_suma_negativos():
    assert suma(-2, -3) == -5

def test_suma_mixta():
    assert suma(-2, 3) == 1

