# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
# Después debe mostrar por pantalla el mensaje “<nombre> tiene <edad> años, vive en <dirección>
# y su número de teléfono es <teléfono>”.

info = {"nombre", "edad", "direccion", "telefono"}
nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
direccion = input("Introduce tu dirección: ")
telefono = input("Introduce tu número de teléfono: ")
print(nombre + " tiene " + edad + " años, vive en " + direccion + " y su número de teléfono es " + telefono)
