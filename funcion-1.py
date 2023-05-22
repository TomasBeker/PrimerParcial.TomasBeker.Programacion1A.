# 1. Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto y
#  devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main.

def aplicar_aumento(precio:float)->float:
    aumento = precio * 0.05
    
    precio_aumentado = precio + aumento

    return precio_aumentado

print(aplicar_aumento(200))