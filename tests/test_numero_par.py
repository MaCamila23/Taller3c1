from funciones.numero_par import par
def test_part():
    assert par(4) == True
    assert par(3) == False