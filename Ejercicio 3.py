#Escribir un programa que guarde en un diccionario los precios de los artículos de la tabla,
#pregunte al usuario por un artículo, un número de unidades y muestre por pantalla el precio de esa cantidad de producto.
#Si el producto no está en el diccionario debe mostrar un mensaje informando de ello.

productos = {"pan": 1.40, "huevos": 2.30, "cebolla": 0.85, "aceite": 4.35}

producto = str.lower(input("Introduce un producto: "))
unidades = int(input("¿Cuántas unidades?: "))

if producto in productos:
    print("El precio de", unidades, "unidades de", producto, "es:", str(productos[producto]*unidades))
else:
    print("No existe el producto")

