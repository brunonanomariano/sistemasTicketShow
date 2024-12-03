from crearUsuario import *

def test_pass_valida():
    assert validarPassword("Pepe123#") == True

def test_pass_invalida():
    assert validarPassword("pepe123") == False

def test_existe_archivo():
    assert existe_archivo("usuarios.json") == True
    
def test_no_existe_archivo():
    assert existe_archivo("archivo.json") == False

def test_existe_usuario():
    assert existeUsuario("prueba", "usuarios.json") == True

def test_no_existe_usuario():
    assert existeUsuario("prueba1", "usuarios.json") == False

def test_mail_valido():
    assert validarEmail("email@email.com") != None

def test_mail_invalido():
    assert validarEmail("mail") == None



