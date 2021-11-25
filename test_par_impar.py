#Correr pytest en consola python -m pytest .\nombre_del_archivo.py

def es_par (num_a,num_b):
    a=0
    b=0
    if num_a%2 == 0 and num_b%2 == 0:
        return True
    else:
        return False

def test_es_par():
    num_a = 2
    num_b = 4
    result = es_par(num_a,num_b)
    assert result , 'Los numeros no son pares'

def test_no_par():
    num_a = 3
    num_b = 3
    result = es_par(num_a,num_b)
    assert not result , 'Los numeros no son impares'
