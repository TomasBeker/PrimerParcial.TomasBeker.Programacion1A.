#2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro,
#  un carácter como segundo y otro carácter  como tercero,  la misma deberá reemplazar cada ocurrencia del segundo 
# parámetro por el tercero y devolver la cantidad de veces que se reemplazo ese carácter  en la cadena'

def reemplazar_caracteres(cadena:str, caracter_reemplazo:str, caracter_nuevo:str)->str:

    cadena_actualizada = cadena.replace(caracter_reemplazo, caracter_nuevo)
    cantidad_reemplazo = cadena.count(caracter_reemplazo)

    return cadena_actualizada , cantidad_reemplazo

print(reemplazar_caracteres("hola como estas", "o", "A"))