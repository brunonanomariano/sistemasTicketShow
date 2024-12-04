from checkout import *

def test_descuento_aplicado():
    assert aplicar_descuento("10%", 1000, {"20%":0.20, "10%":0.10, "5%":0.5}) == 900 

def test_descuento_no_aplicado():
    assert aplicar_descuento("30%", 1000, {"20%":0.20, "10%":0.10, "5%":0.5}) == 1000

def test_tarjeta_valida():
    assert validar_tarjeta("1234567890123456") == True

def test_tarjeta_invalidad():
    assert validar_tarjeta("1234") == False