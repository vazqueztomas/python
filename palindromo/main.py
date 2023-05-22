"""
Problema: dada una cadena de Python, compruebe si es o no un palíndromo.

En caso afirmativo, devuelva Verdadero; de lo contrario, devuelve Falso.
"""

def cheq_palindromo(string: str):
    my_array = list(string)
    my_array_reversed = my_array[::-1]
    es_palindromo = False
    for i in range(len(my_array)):
        if my_array[i] == my_array_reversed[i]:
            es_palindromo = True
        else:
            es_palindromo = False
    return es_palindromo

print(cheq_palindromo('neuquen'))

