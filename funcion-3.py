#3 Crear una función que se llame ordenarCaracteres que reciba una cadena de caracteres como parámetro 
#  y su responsabilidad es ordenar los caracteres de manera ascendente dentro de la cadena.
#  Ejemplo si le pasamos "algoritmo" la deja como "agilmoort"

def ordenar_caracteres(cadena:str):
    
    cadena_ordenada = ''.join(sorted(cadena))

    return cadena_ordenada

print(ordenar_caracteres("algoritmo"))