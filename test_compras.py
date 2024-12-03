from compras import *

def test_separar_fila_asiento():
    assert separar_fila_asiento("A1") == ("A", 0)

def test_coordenadas_correctas():
    assert verificar_coordenadas(["A","B","C"],[0,1,2,3],"A1") == 0

def test_coordenadas_inexistentes():
    assert verificar_coordenadas(["A","B","C"],[0,1,2,3],"D1") == 1
    assert verificar_coordenadas(["A","B","C"],[0,1,2,3],"A5") == 1
    assert verificar_coordenadas(["A","B","C"],[0,1,2,3],"Z9") == 1

def test_formato_coordenadas():
    assert verificar_coordenadas(["A","B","C"],[0,1,2,3],"1A") == 2